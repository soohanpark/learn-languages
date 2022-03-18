#include "stdio.h"

#define DEFAULT_FEE 10000
#define DEFAULT_TEXT_OVER20 20
#define DEFAULT_VOICE_UNDER100 100
#define DEFAULT_VOICE_OVER100 80
#define INCLUDE_VAT 1.1

int voice_charge(int minute);
int text_charge(int times);
int calc(int cost1, int cost2);

void main() {
	int minute, times;

	printf("음성 통화 시간은(분)? ");
	scanf_s("%d", &minute);
	printf("문자 전송 건수는? ");
	scanf_s("%d", &times);

	int cost1 = voice_charge(minute);
	int cost2 = text_charge(times);
	int total = calc(cost1, cost2);

	printf("휴대폰 사용 요금 청구서\n");
	printf("=============================================\n");
	printf("음성 통화 시간 \t%d 분\n", minute);
	printf("문자 전송 건수 \t%d 건\n", times);
	printf("---------------------------------------------\n");
	printf("기본 요금 \t%d원\n", DEFAULT_FEE);
	printf("음성 통화료 %d 분 \t%d원\n", minute, cost1);
	printf("문자 전송료 초과 %d 건(20건 무료) \t%d원\n", times - 20, cost2);
	printf("---------------------------------------------\n");
	printf("합계 \t%d원\n", total);
	printf("부가세(10%%) \t%d원\n", (int)(total*0.1));
	printf("=============================================\n");
	printf("이번 달 요금 \t%d원\n", (int)(total*INCLUDE_VAT));


}

int voice_charge(int minute) {
	if (minute <= 100)
		return minute * DEFAULT_VOICE_UNDER100;
	else
		return minute * DEFAULT_VOICE_OVER100;
}

int text_charge(int times) {
	if (times <= 20)
		return 0;
	else
		return (times-20) * DEFAULT_TEXT_OVER20;
}

int calc(int cost1, int cost2) {
	return (DEFAULT_FEE + cost1 + cost2);
}
