int main() {
    int *ponteiro;
    ponteiro = (int *) (malloc (10 * sizeof(int)));
    ponteiro = (int *) (realloc (22 * sizeof(int)));
    free(ponteiro);
}