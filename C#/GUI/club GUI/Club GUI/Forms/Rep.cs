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
    public partial class Rep : Form
    {
        // Global variable
        string Club;

        public Rep(string club_name)
        {
            InitializeComponent();

            // set global variable
            Club = club_name;

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

        /****************************************Buttons****************************************/

        // Search Clubs
        private void Search_Click(object sender, EventArgs e)
        {
            MoveImageBox(sender);
            showtab(new Search_Club());
        }

        // Weekly Updates
        private void Msg_Click(object sender, EventArgs e)
        {
            MoveImageBox(sender);
            showtab(new Weekly_Updates(Club));
        }

        // Update description
        private void Update_Click(object sender, EventArgs e)
        {
            MoveImageBox(sender);
            showtab(new Update_Club_Description(Club));
        }

        // Goes back to Log in
        private void exit_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Did you post a weekly update?", "Befor you go", MessageBoxButtons.YesNo);

            if (result == System.Windows.Forms.DialogResult.Yes)
            {
                // Go Back
                this.Hide();
                Login login = new Login();
                login.ShowDialog();
            }
            else
            {
                // Highlight the Weekly updates tab
                Msg.Checked = true;
                MoveImageBox(Msg);
                showtab(new Weekly_Updates(Club));
            }
        }
    }
}
