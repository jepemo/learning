#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int num;
} data_t;

int init_data_pp(data_t **data) {
    data_t *new_data = (data_t *) malloc(sizeof(data_t));

    new_data->num = 99;

    *data = new_data;

    return 0;
}

// int test_func(int param1, int param2, int param3, int param4, int param5, int param6, int param7,
//               int param8, int param9, int param10) {
//     int   a = 1;
//     bool  b = true;
//     char *c = "hello";
//     return param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 +
//     param10;
// }

int main(int argc, char **argv) {
    data_t *data = NULL;
    if (init_data_pp(&data) != 0) {
        fprintf(stderr, "Not enough memory initializing data\n");
        exit(EXIT_FAILURE);
    }

    printf("Num is: %d\n", data->num);
    free(data);

    return EXIT_SUCCESS;
}