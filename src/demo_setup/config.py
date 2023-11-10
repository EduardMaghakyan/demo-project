from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


CONFIG: dict = {
    "app": {
        "env": env("APPLICATION_ENV", "dev"),
    },
}
