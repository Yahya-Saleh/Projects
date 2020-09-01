using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Club_GUI
{
    public partial class Student : Form
    {
        public Student()
        {
            InitializeComponent();

            // Displaying first tab
            showtab(new Search_Club());
        }

        /***************************************Navegation******************************************************/

        // For the image slide next to the button
        private void MoveImageBox(object sender)
        {
            Guna.UI2.WinForms.Guna2Button b = (Guna.UI2.WinForms.Guna2Button) sender;

            pb.Location = new Point(b.Location.X + 6, b.Location.Y - 45);
            // Ensure the slider is back
            pb.SendToBack();
        }

        // Displays a given UserControl, i.e. tab
        private void showtab(UserControl uc)
        {
            // Clear any prevoius display
            panelcontrol.Controls.Clear();

            uc.Dock = DockStyle.Fill;
            uc.BringToFront();

            panelcontrol.Controls.Add(uc);
        }

        /***************************************Buttons******************************************************/

        // Search Clubs
        private void Search_Click(object sender, EventArgs e)
        {
            MoveImageBox(sender);
            showtab(new Search_Club());
        }

        private void Register_Click(object sender, EventArgs e)
        {
            MoveImageBox(sender);
            showtab(new Register_to_Club());
        }

        // Goes back to Log in
        private void exit_Click(object sender, EventArgs e)
        {
            this.Hide();
            Login login = new Login();
            login.ShowDialog();
        }
    }
}
