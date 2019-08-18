'''
???????????****Frequently asked 05
https://www.geeksforgeeks.org/microsofts-asked-interview-questions/
https://www.geeksforgeeks.org/print-last-10-lines-of-a-given-file/

Print last 10 lines of a big file or big string.
Given some text lines in one string, each line is separated by ‘\n’ character. Print the last ten lines. 
If number of lines is less than 10, then print all lines.
Source: Microsoft Interview | Set 10

Following are the steps
1) Find the last occurrence of DELIM or ‘\n’
2) Initialize target position as last occurrence of ‘\n’ and count as 0 , and do following while count < 10
……2.a) Find the next instance of ‘\n’ and update target position
…..2.b) Skip ‘\n’ and increment count of ‘\n’ and update target position
3) Print the sub-string from target position.

sample text file to read: https://sample-videos.com/download-sample-text-file.php


SOLUTION
python seek function!!!
seek() sets the file’s current position at the offset. (Absolute file positioning)
Any argument is optional and 
defaults to 0, which means absolute file positioning, 
other values are 1 which means seek relative to the current position and 
2 means seek relative to the file’s end. 
There is no return value.

f.seek(n) #파일의 n번째 바이트로 이동
f.seek(n, 1) #현재 위치에서 n 바이트 이동 n양수면 뒤쪽으로 음수면 앞쪽으로
f.seek(n, 2) #맨 마지막에서 n바이트로 이동 (n은 보통 음수)
f.tell() #현재의 파일 포인터 위치를 반환



'''
def tail(file, n=1, bs=1024):
        
    with open(file, "r") as f:
        f.seek (0, 2)           # Seek @ EOF
        fsize = f.tell()        # Get Size
        f.seek (max (fsize-bs, 0), 0) # Set pos @ last n chars
        print('f.seek is at {}'.format(f.readline(1)))
        lines = f.readlines()       # Read to end

    lines = lines[-n:]    # Get last n lines
    return lines   
    
lines = tail("SampleTextFile_10kb.txt", 2)
for line in lines:
	print (line)