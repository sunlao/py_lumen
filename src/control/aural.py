from subprocess import run
from time import sleep

AUDIO_DEVICE = "plughw:2,0"
AUDIO_FILE = "/home/cp/Music/PushPushDisco.wav"

def volume() -> None:
    controls = ["PCM", "Headphone",]
    for control in controls:
        result = run(
            ["amixer", "-c", "2", "set", control, "100%",],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"volume set using: {control}")
            return
    print("no matching mixer control found")


def play() -> None:
    run(["aplay", "-D", AUDIO_DEVICE, AUDIO_FILE,], check=True)


def execute() -> None:
    volume()
    while True:
        play()


if __name__ == "__main__":
    execute()
