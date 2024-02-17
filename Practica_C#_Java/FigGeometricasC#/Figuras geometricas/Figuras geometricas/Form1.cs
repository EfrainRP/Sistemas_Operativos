using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Figuras_geometricas
{
    public partial class Form1 : Form
    {
        Cuadrado cuadrado;
        Triangulo triangulo;
        Rectangulo rectangulo;
        Poligono poligono;
        public Form1()
        {
            InitializeComponent();
        }

        private void Base_TextChanged(object sender, EventArgs e)
        {

        }
        private void Altura_TextChanged(object sender, EventArgs e)
        {

        }
        private void calcular_Click(object sender, EventArgs e)
        {
            //Verificara que los datos INPUT sean numeros
            double base_, altura_;
            bool baseNum = double.TryParse(Base.Text, out base_);
            bool alturaNum = double.TryParse(Altura.Text, out altura_);

            String figuraUI = listFig.SelectedItem.ToString();
            if (baseNum && alturaNum && base_>=0 && altura_>=0)
            {
                if (figuraUI.Equals("Cuadrado"))
                {
                    cuadrado = new Cuadrado();
                    cuadrado.setLado1(base_);
                    cuadrado.setLado2(altura_);
                    cuadrado.calcularArea();
                    Area.Text = cuadrado.getArea().ToString();
                }
                else if (figuraUI.Equals("Triangulo"))
                {
                    triangulo = new Triangulo();
                    triangulo.setBase(base_);
                    triangulo.setAltura(altura_);
                    triangulo.calcularArea();
                    Area.Text = triangulo.getArea().ToString();
                }
                else if (figuraUI.Equals("Rectangulo"))
                {
                    rectangulo = new Rectangulo();
                    rectangulo.setBase(base_);
                    rectangulo.setAltura(altura_);
                    rectangulo.calcularArea();
                    Area.Text = rectangulo.getArea().ToString();
                }
                else if (figuraUI.Equals("Poligono"))
                {
                    poligono = new Poligono();
                    poligono.setPerimetro(base_);
                    poligono.setApotema(altura_);
                    poligono.calcularArea();
                    Area.Text = poligono.getArea().ToString();
                }
            }
            else
            {
                // Mostrar el MessageBox
                MessageBox.Show("Valor no Aceptado", "Error");
                Area.Clear();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listFig.SelectedIndex = 0; //Se configura valor por defecto
        }
    }
}
