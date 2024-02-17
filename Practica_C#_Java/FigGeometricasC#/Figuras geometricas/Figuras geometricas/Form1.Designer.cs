namespace Figuras_geometricas
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.Calcular = new System.Windows.Forms.Button();
            this.listFig = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.Base = new System.Windows.Forms.TextBox();
            this.Altura = new System.Windows.Forms.TextBox();
            this.Area = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // Calcular
            // 
            this.Calcular.Location = new System.Drawing.Point(221, 157);
            this.Calcular.Name = "Calcular";
            this.Calcular.Size = new System.Drawing.Size(75, 23);
            this.Calcular.TabIndex = 0;
            this.Calcular.Text = "Calcular";
            this.Calcular.UseVisualStyleBackColor = true;
            this.Calcular.Click += new System.EventHandler(this.calcular_Click);
            // 
            // listFig
            // 
            this.listFig.FormattingEnabled = true;
            this.listFig.Items.AddRange(new object[] {
            "Cuadrado",
            "Triangulo",
            "Rectangulo",
            "Poligono"});
            this.listFig.Location = new System.Drawing.Point(282, 75);
            this.listFig.Name = "listFig";
            this.listFig.Size = new System.Drawing.Size(121, 21);
            this.listFig.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 37);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(130, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Lado / Base / Perimetro : ";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(12, 75);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(128, 13);
            this.label2.TabIndex = 3;
            this.label2.Text = "Lado / Altura / Apotema :";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(102, 123);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(38, 13);
            this.label3.TabIndex = 4;
            this.label3.Text = "Area : ";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(279, 58);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(113, 13);
            this.label4.TabIndex = 5;
            this.label4.Text = "Seleccione una figura:";
            // 
            // Base
            // 
            this.Base.Location = new System.Drawing.Point(148, 34);
            this.Base.Name = "Base";
            this.Base.Size = new System.Drawing.Size(100, 20);
            this.Base.TabIndex = 6;
            this.Base.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.Base.TextChanged += new System.EventHandler(this.Base_TextChanged);
            // 
            // Altura
            // 
            this.Altura.Location = new System.Drawing.Point(148, 75);
            this.Altura.Name = "Altura";
            this.Altura.Size = new System.Drawing.Size(100, 20);
            this.Altura.TabIndex = 7;
            this.Altura.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.Altura.TextChanged += new System.EventHandler(this.Altura_TextChanged);
            // 
            // Area
            // 
            this.Area.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.Area.Enabled = false;
            this.Area.Location = new System.Drawing.Point(148, 120);
            this.Area.Name = "Area";
            this.Area.ReadOnly = true;
            this.Area.Size = new System.Drawing.Size(100, 20);
            this.Area.TabIndex = 8;
            this.Area.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(435, 193);
            this.Controls.Add(this.Area);
            this.Controls.Add(this.Altura);
            this.Controls.Add(this.Base);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.listFig);
            this.Controls.Add(this.Calcular);
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Figuras Geometricas";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button Calcular;
        private System.Windows.Forms.ComboBox listFig;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox Base;
        private System.Windows.Forms.TextBox Altura;
        private System.Windows.Forms.TextBox Area;
    }
}

