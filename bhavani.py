import math
import random
#prompt_hr = input('Enter the hours worked: ')
#prompt_rt = input('Enter the hourly rate: ')

#try:
#	hr = float(prompt_hr)
#	rt = float(prompt_rt)
#except:
#	print('Error, please enter numeric input')
#quit()
#
#if hr > 40:
#	total_pmt = hr * rt * 1.5
#else:
#	total_pmt = hr * rt
#
#print('Pay: ' + str(total_pmt))


#prompt_score = input('Input score between 0.0 and 1.0 : ')
#try:
#	score = float(prompt_score)
#except:
#	print('Bad Score')
#	quit()
#
#if score > 1.0:
#	print('Score is outside range')
#	quit()
#elif	score>= 0.9:
#	print('Grade is : A')
#elif	score>= 0.8:
#	print('Grade is : B')
#elif	score>= 0.7:
#	print('Grade is : C')
#elif 	score>= 0.6:
#	print('Grade is : D')
#elif	score< 0.6:
#	print('Grade is : F')
#else:
#	print('Bad Score')
	
#print(math.sqrt(2)/2)

#for i in range(10):
#	x=random.random()
#	print(x)

	
#def repeat_func():
#	first_function()
#	first_function()

#def first_function():
#	print('This is my first song !')
#	print('Tell me what and where it is wrong !')

#repeat_func()

# def fred():
	# print("Zap")

# def jane():
	# print("ABC")

# jane()
# fred()
# jane()

# def compute_pay(prompt_hr,prompt_rt):
	# try:
		# hr = float(prompt_hr)
		# rt = float(prompt_rt)
		# if hr > 40:
			# total_pmt = hr * rt * 1.5
		# else:
			# total_pmt = hr * rt
	# except:
		# print('Error, please enter numeric input')
	
	# print('Pay: ' + str(total_pmt))
	
# compute_pay(50,10)

# def grading():
	# prompt_score = input('Input score between 0.0 and 1.0 : ')
	# try:
		# score = float(prompt_score)
	# except:
		# print('Bad Score')
		# quit()

	# if score > 1.0:
		# print('Score is outside range')
		# quit()
	# elif	score>= 0.9:
		# print('Grade is : A')
	# elif	score>= 0.8:
		# print('Grade is : B')
	# elif	score>= 0.7:
		# print('Grade is : C')
	# elif 	score>= 0.6:
		# print('Grade is : D')
	# elif	score< 0.6:
		# print('Grade is : F')
	# else:
		# print('Bad Score')

# grading()

# while True:
		# line = input('Input your line: ')
		# if line[2] == '&' :
			# print('Nothing to print. Continue')
			# continue
		# if line == 'done':
			# break
		# print(line)
# print('Done')
			



# tot = 0
# cnt = 0
# avg = 0
# min_val = 0
# max_val = 0
# while True:
	# inp_num = input('number: ')
	# try:
		# if inp_num == 'done':
			# break
		# for i in [float(inp_num)]:
			# tot = float(tot) + i
			# cnt = float(cnt) + 1
			# avg = float(tot) / cnt
			# if i < float(min_val):
				# min_val = i
			# if i > float(max_val):
				# max_val = i
	# except:
		# print('Bad Number')
# print ('Total is: '+ str(tot))
# print('Count is: '+ str(cnt))
# print('Average is: '+ str(avg))
# print('Minimum is: '+ str(min_val))
# print('Maximum is: '+ str(max_val))
		
# name = input('Input the name: ')
# str_len = len(name)

# while str_len>0:
	# letter = name[str_len-1]
	# print(letter)
	# str_len = str_len-1

# name = input('Input the name: ')
# letter = input('Input the letter: ')
# occur = 0
# j = 0
# for i in name[:]:
	# if name[j] == letter:
		# occur = occur + 1
	# j = j+1
# print(occur)

#def char_count(word,letter):
# word = input('Input the name: ')
# letter = input('Input the letter: ')
# occur = 0
# for i in word[:]:
	# if i == letter:
		# occur = occur + 1
# print(occur)	

# word = input('Input the name: ')
# letter = input('Input the letter: ')
# print(word.count(letter))	

# fname = input('Enter the file name: ')

# try:
	# fopen = open(fname)
# except:
	# print('File not found')

# for line in fopen:
	# line = line.rstrip()
	# if line.startswith('X-Sieve:'): 
		# exit()
	# print(line.upper())
	
# fname = input('Enter the file name: ')
# index = 0
# cnt = 0
# total = 0
# try:
	# fopen = open(fname)
# except:
	# print('File not found')
# for line in fopen:
	# if line.startswith('X-DSPAM-Confidence: '):
		# cnt = cnt + line.count('X-DSPAM-Confidence: ')
		# length = len('X-DSPAM-Confidence: ')
		# total = total + float(line[length:])
		# average = float(total)/float(cnt)
# print(total)
# print('Average spam confidence: ' + str(average))
# print(cnt)

# import re

# fname = input('Enter the file name: ')
# index = 0
# cnt = 0
# total = 0
# try:
	# fopen = open(fname)
# except:
	# print('File not found')
# for line in fopen:
	# if line.startswith('X-DSPAM-Confidence: '):
		# cnt = cnt + line.count('X-DSPAM-Confidence: ')
		# total = total + float(re.findall('\d\.\d{4,5}',line)[0]) ##RegEx expression '\d\.\d{4,5}' is to find the decimals that are returned in a list which can have 4 or 5 decimal points. This is returned as a list and hence [0]
# average = float(total)/float(cnt)
# print('Total spam confidence: ' + str(total))
# print('Average spam confidence: ' + str(average))
# print('Count of spam confidence: ' + str(cnt))


# fname = input('Enter the file name: ')
# try:
	# fopen = open(fname)
# except:
	# print('File not found')
# for object in range(len(metaDataObjects)):
	# print(fopen[object])
	
# num_list = list()
# try:
	# while True:
		# numbr = input('Enter the value:')
		# if numbr == 'done': break
		# num_list.append(float(numbr))
	# print('Sum is: '+str(sum(num_list)))
	# print('Count. is: '+str(len(num_list)))
	# print('Avg. is: '+str(sum(num_list)/len(num_list)))
# except:
	# print('Pls enter a valid number')

# myfile = open('metadataFull.json')
# for line in myfile:
	# line = line.rstrip()
	# #print(line.find('name'))
	# if  line.find('name') < 0: continue
	# words = line.split()
	# print(words[:])


# def chop(t):
	# del(t[0])
	# del(t[-1])
	
# my_list = [1,2,3,4,5]
# t2 = chop(my_list)
# print(my_list)
# t3 = my_list
# print(t2)
# print(t3)

# f = input('Enter the file name:')
# myword_list=list()
# fname = open(f)
# i=0
# for line in fname:
	# line = line.rstrip()
	# words = line.split()
	# for i in words:
		# if i in myword_list : continue
		# mylist = myword_list.append(i)
# myword_list.sort()
# print(myword_list)

# word = 'brontosaurus'
# d = dict()
# for c in word:
	# d[c] = d.get(c,0) + 1
# print(d)

# prompt = input('Enter the file name: ')
# fname = open(prompt)
# mydict = dict()
# for line in fname:
	# words = line.split()
	# for word in words:
		# if word not in mydict: 
			# mydict[word] = 1
		# else:
			# mydict[word]+=1
	# cnt = list(mydict.keys())
	# cnt.sort()
# for key in cnt:
	# print(key,mydict[key])
		
# import string		
# prompt = input('Enter the file name: ')
# fname = open(prompt)
# mydict = dict()
# for line in fname:
	# line.rstrip()
	# line = line.translate(line.maketrans('','',string.punctuation))
	# words = line.split()
	# print(words[3])
	# for word in words:
		# if word not in mydict:
			# mydict[word] = 1
		# else:
			# mydict[word] += 1

##################################################PAGE 122: Exercise 3:
# import string		
# prompt = input('Enter the file name: ')
# fname = open(prompt)
# mydict = dict()
# mylist = list()
# for line in fname:
	# line.rstrip()
	# #line = line.translate(line.maketrans('','',string.punctuation))	
	# words = line.split()
	# if line.startswith('From '): 
		# my_word = words[2]
		# if my_word not in mydict:
			# mydict[my_word] = 1
		# else:
			# mydict[my_word]+=1
# print(mydict)
##################################################PAGE 122: Exercise 4:
# import string		
# prompt = input('Enter the file name: ')
# fname = open(prompt)
# mydict = dict()
# mylist = list()
# for line in fname:
	# line.rstrip()
	# #line = line.translate(line.maketrans('','',string.punctuation))	
	# words = line.split()
	# if line.startswith('From ') and line.find('@')>0: 
		# my_word = words[1]
		# if my_word not in mydict:
			# mydict[my_word] = 1
		# else:
			# mydict[my_word]+=1
# max_occ = max(mydict.values())
# for key in mydict:
	# if mydict[key] == max_occ: print(key, mydict[key])

##################################################PAGE 122: Exercise 5:	

# import string
# prompt = input('Enter the file name:')
# fname = open(prompt)
# mydict = dict()
# for line in fname:
	# line.rstrip()
	# word = line.split()
	# if line.startswith('From '):
		# my_str = word[1]
		# pos = my_str.find('@')
		# length = len(my_str)
		# substr = my_str[pos+1:length]
		# if substr not in mydict:
			# mydict[substr] = 1
		# else:
			# mydict[substr] += 1
# print(mydict)

##################################################PAGE 122: Exercise 5:	Same program but using tuples functionality on line 389
# import string
# prompt = input('Enter the file name:')
# fname = open(prompt)
# mydict = dict()
# for line in fname:
	# line.rstrip()
	# word = line.split()
	# if line.startswith('From '):
		# my_str = word[1]
		# fn, ln = my_str.split('@')
		# #print(fn, ln)
		# if ln not in mydict:
			# mydict[ln] = 1
		# else:
			# mydict[ln] += 1
# print(mydict.items())

import string
#prompt = input('Enter the file name:')
fname = open("C:\\Suryas\\My_Repos\\Coding-Dojo\\romeo.txt")
mydict = dict()
for line in fname:
	line.rstrip()
	line = line.translate(str.maketrans('','',string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in mydict: 
			mydict[word] = 1
		else: 
			mydict[word] += 1
lst = list()
for (val,key) in mydict.items():
	lst.append((val,key))
	lst.sort(reverse = True)
	#print(val,key)
for (key,val) in lst[:10]:
	print(key, val)
	