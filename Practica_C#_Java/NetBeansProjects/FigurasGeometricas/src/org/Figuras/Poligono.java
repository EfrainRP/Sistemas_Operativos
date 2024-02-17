package org.Figuras;

public class Poligono extends Figuras{
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

    public void calcularArea()
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
