if __name__ == '__main__':
    my_list= []
    list_of_scores = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        list_of_scores.append(score)
        student.append(name)
        student.append(score)
        my_list.append(student)
    
    list_of_scores.sort()
    second_lowest_score = list_of_scores[1]
    final_answer = []
    for item in my_list:
        if item[1] == second_lowest_score:
            final_answer.append(item[0])
        final_answer.sort()
    for name in final_answer:
        print(name)
