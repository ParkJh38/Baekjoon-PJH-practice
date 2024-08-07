# [Bronze IV] 빠른 A+B - 15552 

[문제 링크](https://www.acmicpc.net/problem/15552) 

---
**input()**

input()이 호출되면 인자로 주어진 문자를 화면에 출력하고 사용자의 입력을 기다린다.
사용자가 키를 누르면 그에 대응하는 데이터가 하나씩 버퍼에 들어간다.
개행 문자는 입력의 종료로 간주한다.
무엇을 입력하든 문자열로 변환하고 줄 바꿈을 제거한 뒤 값을 반환한다.

**sys.stdin.readline()**

input()과 달리 문자를 화면에 출력하는 기능이 없다.
한 번에 읽을 수 있는 글자 수 크기에 대한 매개변수를 제공한다.
한 번에 읽어와 버퍼에 저장한다. 따라서 하나 씩 누를 때마다 데이터를 버퍼에 저장하는 input() 보다 빠르며 입력이 많아질수록 차이가 더욱 커진다.

**결론**

input()은 문자열 변환 줄 바꿈 제거 등 추가적인 과정이 있고, 데이터가 하나씩 버퍼에 들어가는 반면, sys.stdin.readline()은 문자열로 변환, 줄 바꿈 과정이 없으며 데이터가 한번에 버퍼에 들어가므로 sys.stdin.readline()이 input()보다 빠르다.

---

### 성능 요약

메모리: 31120 KB, 시간: 1300 ms

### 분류

구현, 사칙연산, 수학

### 제출 일자

2024년 8월 7일 18:02:12

### 문제 설명

<p>본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.</p>

<p>C++을 사용하고 있고 <code>cin</code>/<code>cout</code>을 사용하고자 한다면, <code>cin.tie(NULL)</code>과 <code>sync_with_stdio(false)</code>를 둘 다 적용해 주고, <code>endl</code> 대신 개행문자(<code>\n</code>)를 쓰자. 단, 이렇게 하면 더 이상 <code>scanf</code>/<code>printf</code>/<code>puts</code>/<code>getchar</code>/<code>putchar</code> 등 C의 입출력 방식을 사용하면 안 된다.</p>

<p>Java를 사용하고 있다면, <code>Scanner</code>와 <code>System.out.println</code> 대신 <code>BufferedReader</code>와 <code>BufferedWriter</code>를 사용할 수 있다. <code>BufferedWriter.flush</code>는 맨 마지막에 한 번만 하면 된다.</p>

<p>Python을 사용하고 있다면, <code>input</code> 대신 <code>sys.stdin.readline</code>을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 <code>.rstrip()</code>을 추가로 해 주는 것이 좋다.</p>

<p>또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.</p>

<p>자세한 설명 및 다른 언어의 경우는 <a href="http://www.acmicpc.net/board/view/22716">이 글</a>에 설명되어 있다.</p>

<p><a href="http://www.acmicpc.net/blog/view/55">이 블로그 글</a>에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.</p>

### 입력 

 <p>첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.</p>

### 출력 

 <p>각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.</p>

