using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Club_GUI
{
    public partial class Register_to_Club : UserControl
    {
        public Register_to_Club()
        {
            InitializeComponent();
        }

        // Displays a give category into the combobox
        private void showcat(string cat_name)
        {
            // Clear the comboBox
            cmbClub.Items.Clear();

            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Clubs WHERE Cat=@cat_name ORDER BY State, ClubName;");
            con.cmd.Parameters.AddWithValue("@cat_name", cat_name);

            foreach (DataRow dr in con.QueryEx().Rows)
            {
                cmbClub.Items.Add(dr[0].ToString());
            }

            // Close Connection
            con.con.Close();
        }

        /*********************************************Radio Buttons********************************************/

        private void Art_CheckedChanged(object sender, EventArgs e)
        {
            showcat("ArtOrganization");
        }

        private void Academic_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Academic");
        }

        private void Sport_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Sport");
        }

        // Registers User
        private void Register_Click(object sender, EventArgs e)
        {
            if (cmbClub.SelectedIndex > -1)
            {
                DialogResult result = MessageBox.Show("Are you sure that you want to apply to " + cmbClub.SelectedItem + "? ", "Confirmation", MessageBoxButtons.YesNo);

                if (result == System.Windows.Forms.DialogResult.Yes)
                {
                    MessageBox.Show("Your request has been sent, you will recieve an email once the Club views your request", "Success");
                }
            }
            else
            {
                MessageBox.Show("No item selected", "Error");
            }
        }
    }
}
