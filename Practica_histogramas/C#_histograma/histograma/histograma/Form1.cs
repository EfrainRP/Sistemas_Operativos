using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace histograma
{
    public partial class Form1 : Form
    {
        int[] conjunto = { 5, 8, 9, 2, 7, 4, 2, 1, 3, 6 };
        String [] datos = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        Burbuja b;
        public Form1()
        {
            InitializeComponent();
            b = new Burbuja(conjunto);
        }

        private void btnOrdenar_Click(object sender, EventArgs e)
        {
            b.ordenar();
            conjunto = b.getConjunto();

            System.Windows.Forms.DataVisualization.Charting.Series series = this.chartHistograma.Series.Add("Total: ");
            this.chartHistograma.Series.Clear();

            this.chartHistograma.Palette = ChartColorPalette.SeaGreen;
            this.chartHistograma.Titles.Add("Ventas");
            for(int i = 0; i < conjunto.Length; i++)
            {
                series = this.chartHistograma.Series.Add(datos[i]);
                series.Points.Add(conjunto[i]);
            }

        }
    }
}
