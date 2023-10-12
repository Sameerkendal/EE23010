#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void uniform(char *str, int len);
void desiredDist(char *input_file, char *output_file, int length);
double desired_prob(char *req);

void uniform(char *str, int len) {
    int i;
    FILE *fp;
    fp = fopen(str, "w");

    for (i = 0; i < len; i++) {
        // Generating the standard uniform distribution
        fprintf(fp, "%lf\n", (double)rand() / RAND_MAX);
    }

    fclose(fp);
}

void desiredDist(char *str, char *req, int length) {
    FILE *fp, *dp;
    double x = 0.0;
    double result = 0.0;
    double p = 0.5;

    fp = fopen(str, "r");
    dp = fopen(req, "w");


    while (fscanf(fp, "%lf", &x) != EOF) {

        if (x >= 0 && x < 0.25) {
            result = 0;
        } else if (x >=0.25 && x < 0.75) {
            result = 1;
        } else if (x >= 0.75 && x < 1) {
            result = 2;
        }

        fprintf(dp, "%lf\n", result);
    }

    fclose(fp);
    fclose(dp);
}

double desired_prob(char *req) {
    FILE *dp;
    dp = fopen(req, "r");
    double x = 0.0;
    double prob = 0.0;

    int des_count = 0;
    int act_count = 0;
        while (fscanf(dp, "%lf", &x) != EOF){
        if (x !=0) {
            des_count++;
        }
        act_count++;
    }

    fclose(dp);
    prob = (double)des_count / (double)act_count;
    return prob;
}



int main(void) {
    int len = 100000;

    uniform("uni.dat", len);
    desiredDist("uni.dat", "des_dist.dat", len);

    double act_prob = 3.0 / 4;
    double sim_prob = desired_prob("des_dist.dat");

    printf("The Actual Probability %lf\n", act_prob);
    printf("The Simulated Probability %lf\n", sim_prob);

    return 0;
}

