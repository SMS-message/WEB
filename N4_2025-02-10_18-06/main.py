def format_text_block(frame_height: int, frame_width: int, file_name: str) -> str:
    try:
        with open(file_name, mode="r") as file:
            data = file.read(frame_width * frame_height)
            res = []

            curr_string = ""
            for i, sym in enumerate(data):
                if len(curr_string) >= frame_width:
                    res.append(curr_string)
                    if data[i + 1] != "\n":
                        res.append("\n")
                    curr_string = ""
                if res.count("\n") >= frame_height:
                    break
                if sym == "\n":
                    res.append(curr_string)
                    res.append(sym)
                    curr_string = ""
                else:
                    curr_string += sym

            return "".join(res[:-1])

    except Exception as err:
        return err.__str__()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--frame-height", type=int)
    parser.add_argument("--frame-width", type=int)
    parser.add_argument("file", type=str)

    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.file))


if __name__ == '__main__':
    main()
