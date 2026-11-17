"""Génère les visuels procéduraux du site (parquets anciens). Remplacez-les par vos vraies photos de chantier dès que possible."""
import numpy as np, math, os, sys
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
OUT = sys.argv[1] if len(sys.argv) > 1 else "public/img"
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(7)

def smooth_noise(h, w, scale, seed):
    r = np.random.default_rng(seed)
    gh, gw = max(2, h // scale + 2), max(2, w // scale + 2)
    g = r.random((gh, gw)).astype(np.float32)
    img = Image.fromarray((g * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(img, dtype=np.float32) / 255.0

def plank_tex(Lp, Wp, seed, tone):
    """Texture d'une lame (Lp x Wp) avec veinage de chêne."""
    r = np.random.default_rng(seed)
    y = np.arange(Wp)[:, None].astype(np.float32); x = np.arange(Lp)[None, :].astype(np.float32)
    n1 = smooth_noise(Wp, Lp, 40, seed); n2 = smooth_noise(Wp, Lp, 9, seed + 1)
    freq = r.uniform(0.18, 0.35); phase = r.uniform(0, 6.28)
    warp = n1 * r.uniform(4, 9) + np.sin(x / r.uniform(120, 260) + phase) * r.uniform(1.5, 4)
    grain = np.sin((y + warp) * freq * 2.2) * 0.5 + 0.5
    grain = grain ** 3
    fine = smooth_noise(Wp, Lp, 2, seed + 2)
    rays = (smooth_noise(Wp, Lp, 3, seed + 3) > 0.82).astype(np.float32) * 0.08  # maillure du chêne
    v = 0.62 + 0.18 * n2 - 0.22 * grain + 0.06 * fine + rays
    v *= r.uniform(0.85, 1.12)
    base = np.array(tone, np.float32)
    rgb = np.clip(v[..., None] * base[None, None, :], 0, 255)
    return rgb

def finish(arr, mode):
    a = arr.astype(np.float32)
    if mode == "worn":
        g = a.mean(axis=2, keepdims=True)
        a = a * 0.45 + g * 0.55; a = a * 0.95 + np.array([18, 16, 14])
        h, w, _ = a.shape
        stains = smooth_noise(h, w, 120, 99)
        a *= (0.8 + 0.25 * stains)[..., None]
        img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        d = ImageDraw.Draw(img, "RGBA")
        r = np.random.default_rng(3)
        for _ in range(260):
            x0, y0 = r.uniform(0, w), r.uniform(0, h); ang = r.uniform(0, 3.14); L = r.uniform(20, 160)
            d.line([(x0, y0), (x0 + L * math.cos(ang), y0 + L * math.sin(ang))], fill=(235, 230, 220, int(r.uniform(30, 90))), width=1)
        for _ in range(25):
            x0, y0 = r.uniform(0, w), r.uniform(0, h); s = r.uniform(20, 90)
            d.ellipse([x0, y0, x0 + s, y0 + s * 0.7], fill=(40, 30, 20, 35))
        return img.filter(ImageFilter.GaussianBlur(0.4))
    # vitrifié / huilé : lumière de fenêtre + brillance
    h, w, _ = a.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    light = np.exp(-((xx - w * 0.72) * 0.6 + (yy - h * 0.25)) ** 2 / (2 * (w * 0.22) ** 2))
    vign = 1 - 0.35 * (((xx - w / 2) / w) ** 2 + ((yy - h / 2) / h) ** 2) * 2
    a = a * vign[..., None] * (1.0 + 0.10 * (mode == "oiled")) + light[..., None] * (70 if mode == "varnish" else 40)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))

def joints(canvas_rgb, mask_edges):
    canvas_rgb[mask_edges] *= 0.45
    return canvas_rgb

def chevron(w, h, W=46, C=230, tone=(205, 150, 92)):
    """Point de Hongrie : bandes de largeur C, lames coupées à 45°."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    col = np.floor(xx / C).astype(int); lx = xx - col * C
    sign = np.where(col % 2 == 0, 1.0, -1.0)
    u = yy + sign * (lx if True else 0) * 1.0  # 45°
    u = np.where(col % 2 == 0, yy + lx, yy + (C - lx))
    idx = np.floor(u / W).astype(int); lv = u - idx * W
    out = np.zeros((h, w, 3), np.float32)
    texs = {}
    along = lx * 1.41
    for key in np.unique(col * 10000 + idx):
        c, i = divmod(int(key), 10000)
        texs[key] = plank_tex(int(C * 1.45) + 2, W + 2, seed=abs(c * 977 + i * 131) % 100000, tone=tone)
    keys = col * 10000 + idx
    for key, tex in texs.items():
        m = keys == key
        ys = np.clip(lv[m].astype(int), 0, tex.shape[0] - 1); xs = np.clip(along[m].astype(int), 0, tex.shape[1] - 1)
        out[m] = tex[ys, xs]
    edge = (lv < 1.6) | (lx < 1.5)
    return joints(out, edge)

def herringbone(w, h, L=280, W=56, tone=(196, 140, 84)):
    """Bâton rompu : tracé dans un repère droit puis tourné de 45°."""
    S = int(max(w, h) * 1.5)
    canvas = Image.new("RGB", (S, S), (60, 40, 25))
    k_range = range(-S // W - 8, S // W + 8)
    m_range = range(-S // L - 8, S // L + 8)
    seed = 0
    for m in m_range:
        for k in k_range:
            ox, oy = k * W + m * L, k * W - m * L
            for horiz in (True, False):
                seed += 1
                if horiz: x0, y0, pw, ph = ox, oy, L, W
                else: x0, y0, pw, ph = ox + L, oy - L + W, W, L
                if x0 > S or y0 > S or x0 + pw < 0 or y0 + ph < 0: continue
                tex = plank_tex(L, W, seed, tone)
                im = Image.fromarray(tex.astype(np.uint8))
                if not horiz: im = im.rotate(90, expand=True)
                canvas.paste(im, (int(x0), int(y0)))
                ImageDraw.Draw(canvas).rectangle([x0, y0, x0 + pw - 1, y0 + ph - 1], outline=(70, 46, 28))
    canvas = canvas.rotate(45, resample=Image.BICUBIC)
    cx, cy = S // 2, S // 2
    return np.asarray(canvas.crop((cx - w // 2, cy - h // 2, cx - w // 2 + w, cy - h // 2 + h)), np.float32)

def versailles(w, h, P=420, W=40, tone=(190, 136, 82)):
    """Panneaux Versailles simplifiés : cadre + entrelacs diagonaux."""
    out = np.zeros((h, w, 3), np.float32)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    px, py = np.mod(xx, P), np.mod(yy, P)
    pid = (np.floor(xx / P) * 31 + np.floor(yy / P)).astype(int)
    inner = P - 2 * W
    # bande cadre
    frame = (px < W) | (py < W)
    # diagonales intérieures en treillis
    a = np.mod(px - W + py - W, inner / 2); b = np.mod(px - W - (py - W), inner / 2)
    diag = (a < W * 0.9) | (b < W * 0.9)
    seeds = np.where(frame, 1, np.where(diag, 2, 3))
    for s, tn in ((1, tone), (2, tuple(c * 0.93 for c in tone)), (3, tuple(c * 1.04 for c in tone))):
        tex = plank_tex(P, P, 500 + s, tn)
        m = seeds == s
        ty = py.astype(int)[m] % P; tx = px.astype(int)[m] % P
        if s == 2: tx, ty = ty, tx
        out[m] = tex[ty, tx]
    edge = (np.abs(px - W) < 1.2) | (np.abs(py - W) < 1.2) | (px < 1.2) | (py < 1.2) | (np.abs(a - W * 0.9) < 1.0) | (np.abs(b - W * 0.9) < 1.0)
    return joints(out, edge & ~frame | (frame & ((px < 1.2) | (py < 1.2))))

def anglaise(w, h, W=70, tone=(200, 150, 96)):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    row = np.floor(yy / W).astype(int)
    r = np.random.default_rng(11)
    offs = r.uniform(0, 600, size=row.max() + 2)
    lx = xx + offs[row]; Lp = 700
    idx = np.floor(lx / Lp).astype(int); along = lx - idx * Lp; lv = yy - row * W
    out = np.zeros((h, w, 3), np.float32)
    keys = row * 1000 + idx
    for key in np.unique(keys):
        tex = plank_tex(Lp, W, int(key) + 7, tone); m = keys == key
        out[m] = tex[lv[m].astype(int).clip(0, W - 1), along[m].astype(int).clip(0, Lp - 1)]
    return joints(out, (lv < 1.6) | (along < 1.6))

def save(img, name, q=82):
    img.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
    img.convert("RGB").save(os.path.join(OUT, name + ".jpg"), "JPEG", quality=84, optimize=True, progressive=True)

W, H = 1600, 1000
ch = chevron(W, H)
save(finish(ch, "varnish"), "hero-point-de-hongrie")
save(finish(ch, "worn"), "avant-point-de-hongrie")
save(finish(ch, "oiled"), "apres-point-de-hongrie")
hb = herringbone(1200, 800)
save(finish(hb, "varnish"), "baton-rompu")
save(finish(hb, "worn"), "avant-baton-rompu")
vs = versailles(1200, 800)
save(finish(vs, "oiled"), "parquet-versailles")
an = anglaise(1200, 800)
save(finish(an, "varnish"), "parquet-anglaise")
save(finish(chevron(1200, 800, tone=(150, 100, 62)), "oiled"), "teinte-chene-fonce")
save(finish(chevron(1200, 800, tone=(225, 195, 150)), "varnish"), "vitrification-mat")
save(finish(herringbone(1200, 800, tone=(176, 118, 66)), "oiled"), "huilage-cire")

# Image Open Graph 1200x630
og = finish(chevron(1200, 630), "varnish").convert("RGBA")
ov = Image.new("RGBA", og.size, (18, 24, 38, 170)); og = Image.alpha_composite(og, ov)
d = ImageDraw.Draw(og)
fs = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"; fr = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
d.text((80, 170), "SGE", font=ImageFont.truetype(fs, 46), fill=(201, 164, 92))
d.text((80, 240), "Ponçage Parquet", font=ImageFont.truetype(fs, 72), fill=(250, 246, 238))
d.text((80, 325), "Haussmannien", font=ImageFont.truetype(fs, 72), fill=(250, 246, 238))
d.text((80, 440), "Point de Hongrie · Bâton rompu · Versailles — Paris & Île-de-France", font=ImageFont.truetype(fr, 28), fill=(230, 222, 205))
d.text((80, 500), "Devis gratuit sous 24 h · à partir de 70 €/m²", font=ImageFont.truetype(fr, 28), fill=(201, 164, 92))
og.convert("RGB").save(os.path.join(OUT, "og-image.jpg"), "JPEG", quality=88)
print("ok")
