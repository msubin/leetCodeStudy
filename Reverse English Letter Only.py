def reverseEnglishLetterOnly(string):
    input_array = list(string)
    print(input_array)
    left = 0
    right = len(input_array) - 1

    while left < right:
        if input_array[left].isalpha() and input_array[right].isalpha():
            temp_left = input_array[left]
            temp_right = input_array[right]

            input_array[left] = temp_right
            input_array[right] = temp_left

            left += 1
            right -= 1

        elif not input_array[left].isalpha():
            left += 1

        elif not input_array[right].isalpha():
            right -= 1

    print(input_array)
    return "".join(input_array)


print(reverseEnglishLetterOnly("a-bC-dEf-ghIj"))