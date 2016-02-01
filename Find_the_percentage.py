def name_score_function(lists,out_answer):
	out_answer[lists[0]]=[lists[1]]
	for i in range(2,len(lists)):
		out_answer[lists[0]].append(lists[i])
	return out_answer

def average_score(dic_lists, who):
	total=0
	answer=0
	score_numbers=int(len(dic_lists[who]))
	for i in range(0,score_numbers):
		total=total+float(dic_lists[who][i])
	answer = total/score_numbers
	return answer

number_people=int(input())
input_score={}

for numbers in range(0,number_people):
    numbers_score = input()
    numbers_score = numbers_score.split(" ")
    name_score_function(numbers_score, input_score)

who_do_you_want=(input())
average=average_score(input_score, who_do_you_want)
print ("{:.2f}".format(average))