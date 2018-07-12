# 협력하여 프로그램 만들기

## 들어가기전에.....

#### Test Case와 OOP의 중요성

우리는 코딩할 때 쉽게 위에서부터 순서대로 코딩하고 합니다. 작은 프로그램을 만들 때에는 간편할 수 있지만, 만약 **큰**  프로그램을 만든다면 어떨까요?

큰 프로그램을 어찌어찌 완성해서 디버깅을 한다면, 엄청나게 많은 오류가 튀어나올 것입니다. -만약 처음 디버깅할 때 오류가 안난다면, 그건 어쩌면 더 무서운 일일 수도 있습니다- 

그렇다면 이렇게 많은 오류를 쉽게 잡을 수 있을까요? 아마 어디서 오류가 발생했는지 확인하기도 힘들 것 입니다.

그렇기 때문에 우리는 마치 `레고`를 조립하듯이 코딩해야 합니다. 프로그램에 필요한 기능을 작게 세부적으로 나누어 (함수, 클래스)  작은 조각조각 하나가 잘 작동하는지 확인해야 합니다. 그리고 작은 조각들이 모두 잘 작동할 때 합쳐서 우리는 큰 프로그램을 완성할 수 있습니다!

그렇다면 조각들을 잘 나누기 위해서는 무엇이 필요할까요? 바로 **input, output, effect**를 정확하게 잘 정의할 필요가 있습니다. 그리고 이 조각들을 잘 작동하는지 확인하기 위해 **Test Case**를 잘 만드는 것도 중요합니다.

## 문제 설명

저희가 만들 프로그램 myOwnCounter은

1. 수많은 정수값들 중에서 저희가 10-20 사이의 숫자들만 남겨, 
2. 남은 숫자들의 개수가 홀수면 홀수인 수를 남기고, 남은 숫자들의 개수가 짝수면 짝수인 수를 남기고,
3. 최종적으로 서로 다른값들이 몇개 있는지 확인하는 프로그램을 만들 것입니다.

이 각각의 기능들이 필요한 조각이 되어 각자 나누어 완성하게 될 것입니다.

### 예시

- input.txt

6 14 9 2 25 1 15 7 13 11 7 16 26 19 12 15 14

- output

### Functions

- def readInputTextFile(filename)
  - input : 인풋 파일의 이름 (string)
  - output : 인풋 숫자들의 리스트 (list)
  - effect : input file을 읽어 띄어쓰기로 나누어진 int를 list에 넣는다.
- def deleteOutlier(int_list)
  - input : 인풋 숫자들의 리스트 (list)
  - output : 숫자들의 리스트 (list)
  - effect : 10-20 사이가 아닌 outlier를 제거하여 list를 return 한다.
- def remainOddOrEven(int_list)
  - input : 숫자들의 리스트 (list)
  - output : 숫자들의 리스트 (list)
  - effect : 리스트의 크기가 짝수면 짝수만 남기고, 홀수면 홀수만 남긴다.
- def countNumOfUnique(int_list)
  - input : 숫자들의 리스트 (list)
  - output : 정수 (int)
  - effect : list에서 서로 다른 숫자들이 몇 개인지 count한다. 
- def myOwnCounter(filename)
  - input : 인풋 파일의 이름 (string)
  - output : 정수(int)
  - effect : 우리가 최종적으로 원하는 프로그램. 위의 함수들을 활용하여 만든다.



### Funtion example

- readInputTextFile
  - Input
    : input.txt
  - Output
    : [6, 14, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]
- deleteOutlier
  - Input
    : [6, 14, 9, 2, 25, 1, 15, 7, 13, 11, 7, 16, 26, 19, 12, 15, 14]
  - Output
    : [14, 15, 13, 11, 16, 19, 12, 15, 14]
- remainOddOrEven
  - Input
    : [13, 15, 13, 11, 16, 19, 12, 15, 14]
  - Output
    : [13, 15, 13, 11, 19, 15]
- countNumOfUnique
  - input
    : [13, 15, 13, 11, 19, 15]
  - output
    : 4
- myOwnCounter
  - input
    : input.txt
  - output
    : 4

