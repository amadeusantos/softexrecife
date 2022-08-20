public class TratamentoExcecao {
    public static void main(String[] args) {
        try {
            int numero = 100/0;
            System.out.println(numero);
        } catch (Exception e) {
           System.out.println("Erro do tipo '" + e.getLocalizedMessage() + "' encontrado.");
        }
    }
}
