# try:
#     with open("tiktokers.txt") as tiktokers:
#         content = tiktokers.readlines()
#         print(type(content), content)
#         print("the content of the file is", content )
# except FileNotFoundError:
#     print("invalid file")

with open("score_sheets.txt") as scores_file:
    print(scores_file)
    scores = scores_file.readlines()
    score_fix = []

    for score in scores:
        print(score.replace("\n", ""))
        score_fix.append(int(score.replace("\n", "")))
        # print(score)

    # print(sum(scores))
    print(scores)
    print(score_fix)
    print(sum(score_fix))


with open("score_sheets.txt", "a") as scores_file:
    scores_file.writelines(["100\n"])


# with open("actors.txt", "a") as actors_file:
#     actors_file.writelines(["Lalude\n", "RMD\n", "obasanjo\n", "sidi"])
    

# info = "The man killed the dog, and ate the dog at his funeral"

# print(info.replace("dog", "chicken"))


# info = info.replace("dog", "chicken")

# print(info)