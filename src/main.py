def main():
    print("Hello from vscode-setup!")
    number = 1
    new_number = dummie_function(number)
    print(f"Old number: {number}\nNew number: {new_number}")


def dummie_function(var):
    """
    * This is a important info highlight.
    ! this is a warning highlight
    ? this is a question highlight
    TODO: this is a todo highlight
    docstring comment
    """
    # normal comment
    return var + 1


if __name__ == "__main__":
    main()
