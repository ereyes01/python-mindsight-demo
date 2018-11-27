from test import main_module
import sampler


if __name__ == "__main__":
    sampler.start(server_url="http://localhost:8000",project="news_reader",modules=["test"], send_after=10)

    how_many = input("How hard shall I work? (Enter a number): ")

    main_module.spin(how_many)
