
package org.Figuras;

public class Figuras {
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
