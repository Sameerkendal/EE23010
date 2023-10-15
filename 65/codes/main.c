#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void uniform(char *str, int len);
void desiredDist(char *input_file, char *output_file, int length);
double desired_prob(char *req,char *req1);

unsigned long long binomialCoefficient(int n, int k) {
    if (k < 0 || k > n) {
        return 0; // Invalid input
    }

    unsigned long long numerator = 1;
    unsigned long long denominator = 1;

    for (int i = 1; i <= k; i++) {
        numerator *= (unsigned long long)(n - i + 1);
        denominator *= (unsigned long long)i;
    }

    return numerator / denominator;
}

// Function to calculate binomial probability
double binomialProbability(int n, int k, double p) {
    if (k < 0 || k > n || p < 0.0 || p > 1.0) {
        return 0.0; // Invalid input
    }

    double probability = binomialCoefficient(n, k) * pow(p, k) * pow(1 - p, n - k);

    return probability;
}
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

        if (x >= 0 && x < 0.5) {
            result = 0;
        } else if (x >=0.5 && x < 1) {
            result = 1;
        } 
        fprintf(dp, "%lf\n", result);
    }

    fclose(fp);
    fclose(dp);
}

double desired_prob(char *req,char *req1) {
    FILE *dp,*dp1;
    dp = fopen(req, "r");
    dp1 = fopen(req1, "r");
    double x = 0.0;
    double y=0.0;
    double prob = 0.0;

    int des_count = 0;
    int act_count = 0;
        while (fscanf(dp, "%lf", &x) != EOF && fscanf(dp1, "%lf", &y) != EOF){

        if (x+y !=0) {
            des_count++;
        }
        act_count++;
    
}
    fclose(dp);
    fclose(dp1);
    prob = (double)des_count / (double)act_count;
    return prob;
}



int main(void) {
    int len = 100000;
int n=2,k=1;
double p=0.5;
    uniform("uni.dat", len);
    uniform("uni1.dat", len);
    desiredDist("uni.dat", "des_dist.dat", len);
    desiredDist("uni1.dat", "des_dist1.dat", len);	
    double act_prob = binomialProbability(n,k,p)+binomialProbability(n,n,p);
    double sim_prob = desired_prob("des_dist.dat","des_dist1.dat");

    printf("The Actual Probability %lf\n", act_prob);
    printf("The Simulated Probability %lf\n", sim_prob);

    return 0;
}


