from readDatabase import read_halls, read_classes, fetch_rollnos, devide_rollnos
from allotement import main_call
from get_size import main_split


def main(halls, rollnos):
    main_call(halls=halls, rollnos=rollnos)
    # print(g_rows)


if __name__ == '__main__':
    classes = read_classes()
    print(len(classes))
    c = input('classes are fetched')
    rollnos = fetch_rollnos(classes)
    halls = read_halls()
    sizes = main_split(halls=halls,rollno=rollnos)
    c = input('rollnos are fetched')
    divided = devide_rollnos(rollnos,sizes)


    main(rollnos=divided, halls=halls)
