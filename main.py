# python3
from queue import PriorityQueue

def parse_input_user():
    n = list(map(int, input().strip().split(' ')))
    # print(n)
    data = list(map(int, input().strip().split(' ')))
    # print(data)
    return n, data

def parse_input_file(file_name):
    file = open(file_name, "r", -1, "utf-8")
    n = list(map(int, file.readline().strip().split(' ')))
    # print(n)
    data = list(map(int, file.readline().strip().split(' ')))
    # print(data)
    return n, data

def parallel_processing(n, m, data):
    output = []
    queue = PriorityQueue()

    if m <= n:
        for i in range(m):
            print(i, 0)
    else:
        output = [-1 for i in range(len(data))]

        for i in range(n):
            queue.put((data[i], i))
            output[i] = [i, 0]

        for i in range(n, len(data)):
            process = queue.get()
            thread_name = process[1]
            time = process[0]
            output[i] = [thread_name, time]
            queue.put((time + data[i], thread_name))

    return output

def main():
    n, m = 0, 0
    data = []

    try:
        key = input().strip()
        # print(key)
        if (key.upper() == "I"):
            n, m = parse_input_user()
        elif (key.upper() == "F"):
            file_name = input().strip()
            if (file_name.lower() == "a"):
                pass
            n, m = parse_input_file("tests/" + file_name)
    except:
        pass

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for i in result:
        print(i[0], i[1])

if __name__ == "__main__":
    main()
