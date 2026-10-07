import base64
import io
from urllib.parse import urljoin

import qrcode
from django.conf import settings


def generate_qr_base64(url: str) -> str:
    """
    Generate a QR code image for the given URL and return it as a base64-encoded
    data URI (PNG), suitable for use in an <img src="..."> tag.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=6,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="darkgreen", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def build_vote_url(token: str) -> str:
    """
    Build the full public URL for a given token.
    This is the URL that will be encoded in the QR code.
    """
    base = settings.PUBLIC_SITE_URL
    return urljoin(base, f"/{token}/")