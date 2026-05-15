from subprocess import run

AUDIO_DEVICE = "plughw:2,0"
AUDIO_FILE = "/home/cp/Music/PushPushDisco.wav"


def volume() -> None:
    controls = ["PCM", "Headphone"]
    for c in controls:
        result = run(
            ["amixer", "-c", "2", "set", c, "100%"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.returncode == 0:
            print(f"volume set using: {c}")
            return


def play() -> None:
    run(["aplay", "-D", AUDIO_DEVICE, AUDIO_FILE], check=True)


def execute() -> None:
    volume()
    while True:
        play()


if __name__ == "__main__":
    execute()
