using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figuras_geometricas
{
    class Figuras
    {
        protected Double base_;
        protected Double altura_;
        protected Double area_;

        public void setBase(Double base_){
            this.base_ = base_;
        }

        public void setAltura(Double altura_)
        {
            this.altura_= altura_;
        }

        public void calcularArea()
        {
            this.area_= this.altura_*this.base_;
        }

        public Double getBase()
        {
            return this.base_;
        }

        public Double getAltura()
        {
            return this.altura_;
        }

        public Double getArea()
        {
            return this.area_;
        }
    }

    // Figura CUADRADO
    class Cuadrado:Figuras
    {
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

        public new void calcularArea()
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
    // Figura TRIANGULO
    class Triangulo :Figuras
    {
        public new void calcularArea()
        {
            area_ = (this.altura_ * this.base_)/2;
        }
    }
    // Figura RECTANGULO
    class Rectangulo : Figuras { }
    // Figura POLIGONO
    class Poligono :Figuras 
    {
        protected Double perimetro;
        protected Double apotema;

        public void setPerimetro(Double perimetro)
        {
            this.perimetro = perimetro;
        }

        public void setApotema(Double apotema)
        {
            this.apotema = apotema;
        }

        public new void calcularArea()
        {
            area_ = (this.perimetro * this.apotema)/2;
        }

        public Double getPerimetro()
        {
            return this.perimetro;
        }
        public Double getApotema()
        {
            return this.apotema;
        }
    }
}
