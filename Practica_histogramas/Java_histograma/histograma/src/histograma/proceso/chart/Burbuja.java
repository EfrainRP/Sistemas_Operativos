package histograma.proceso.chart;

public class Burbuja {
    private int [] conjunto;
    
    public Burbuja (int [] conjunto){
        this.conjunto = conjunto;
    }
    public void ordenar(){
        int aux=0;
        int i = this.conjunto.length-1;
        int j;
        boolean flag;
        do{
            flag =false;
            j=0;
            while(j<i){
                if (this.conjunto[j] > this.conjunto[j+1]){
                   aux = conjunto[j];
                   conjunto[j]=conjunto[j+1];
                   conjunto[j+1]=aux; 
                   flag=true;
                }
                j++;
            }
            i--;
        }while(flag);
//        for(int i=0;i<this.conjunto.length;i++){
//            for(int j=1;j<this.conjunto.length;j++){
//                if(conjunto[j-1]>conjunto[j]){
//                    aux = conjunto[j];
//                    conjunto[j]=conjunto[j-1];
//                    conjunto[j-1]=aux;
//                }
//            }
//        }
    }
    public int [] getConjunto(){
        return this.conjunto;
    }
}
