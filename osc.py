from pythonosc import udp_client

# Konfiguracja klienta OSC
ip = "192.168.0.94"  # IP Reapera
port = 8000  # Port nasłuchiwania

client = udp_client.SimpleUDPClient(ip, port)


def solo_preset(event):

    # Numer ścieżki
    # track_number = 1

    # Wysłanie komunikatu OSC do Reapera
    client.send_message(f"/track/{2}/solo", 0)
    client.send_message(f"/track/{3}/solo", 0)
    client.send_message(f"/track/{4}/solo", 0)

    client.send_message(f"/track/{2}/mute", 0)
    client.send_message(f"/track/{3}/mute", 0)
    client.send_message(f"/track/{4}/mute", 0)

    client.send_message(f"/track/{2}/solo", 1)  # 1 = mute, 0 = unmute
    client.send_message(f"/track/{3}/mute", 1)
    client.send_message(f"/track/{4}/mute", 1)


def rythm_preset(event):

    # Numer ścieżki
    # track_number = 1

    # Wysłanie komunikatu OSC do Reapera
    client.send_message(f"/track/{2}/solo", 0)
    client.send_message(f"/track/{3}/solo", 0)
    client.send_message(f"/track/{4}/solo", 0)

    client.send_message(f"/track/{2}/mute", 0)
    client.send_message(f"/track/{3}/mute", 0)
    client.send_message(f"/track/{4}/mute", 0)

    client.send_message(f"/track/{2}/mute", 1)  # 1 = mute, 0 = unmute
    client.send_message(f"/track/{3}/solo", 1)
    client.send_message(f"/track/{4}/mute", 1)


def clean_preset(event):

    # Numer ścieżki
    # track_number = 1

    # Wysłanie komunikatu OSC do Reapera
    client.send_message(f"/track/{2}/solo", 0)
    client.send_message(f"/track/{3}/solo", 0)
    client.send_message(f"/track/{4}/solo", 0)

    client.send_message(f"/track/{2}/mute", 0)
    client.send_message(f"/track/{3}/mute", 0)
    client.send_message(f"/track/{4}/mute", 0)

    client.send_message(f"/track/{2}/mute", 1)  # 1 = mute, 0 = unmute
    client.send_message(f"/track/{3}/mute", 1)
    client.send_message(f"/track/{4}/solo", 1)
