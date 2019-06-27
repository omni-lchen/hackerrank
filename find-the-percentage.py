if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for i in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    student_record = student_marks[query_name]
    total = 0
    for i in range(len(student_record)):
        total = total + student_record[i]
    avg = float(total/len(student_record))
    print("%.2f" % avg)
