
package org.Figuras;

public class Cuadrado extends Figuras{ // Figura CUADRADO
    
        protected Double lado1;
        protected Double lado2;

        public void setLado1(Double lado1)
        {
            this.lado1 = lado1;
        }

        public void setLado2(Double lado2)
        {
            this.lado2 = lado2;
        }

        public void calcularArea()
        {
            area_ = this.lado1 * this.lado2;
        }

        public Double getLado1()
        {
            return this.lado1;
        }

        public Double getLado2()
        {
            return this.lado2;
        }
}
