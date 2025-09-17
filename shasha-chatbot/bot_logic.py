def get_bot_response(message, user_data):
    message_low = (message or "").lower()

    if not user_data.get("name"):
        return ("¡Hola! Soy SHASHA. ¿Cómo te llamas?", {"name": None}, False)

    if user_data.get("name") and not user_data.get("phone"):
        return (f"Perfecto, {user_data['name']}. ¿Me das tu número de teléfono?", {"phone": None}, False)

    if user_data.get("name") and user_data.get("phone") and not user_data.get("email"):
        return ("¿Y tu correo electrónico?", {"email": None}, False)

    if "horario" in message_low or "hora" in message_low:
        return ("Nuestro horario es de lunes a viernes de 9:00 a 18:00.", {}, True)

    if "ubicación" in message_low or "dirección" in message_low:
        return ("Nos encontramos en Calle Ejemplo 123, Ciudad.", {}, True)

    if "servicios" in message_low:
        return ("Ofrecemos cortes de cabello, peinados, tintes, etc. ¿Cuál te interesa?", {}, False)

    if "precio" in message_low or "cuánto cuesta" in message_low:
        return ("Nuestros precios empiezan en 20 € para cortes básicos. ¿Qué servicio te interesa?", {}, False)

    if "cita" in message_low or "reservar" in message_low:
        return ("Claro — ¿qué día te vendría bien para la cita? (por ejemplo, 2025‑10‑05)", {}, False)

    return ("Lo siento, no entendí eso. ¿Puedes reformularlo o elegir otra pregunta?", {}, False)
