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
    public partial class Search_Club : UserControl
    {
        public Search_Club()
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

            con.SqlQuery("SELECT * FROM Clubs WHERE Cat=@cat_name");
            con.cmd.Parameters.AddWithValue("@cat_name", cat_name);

            foreach (DataRow dr in con.QueryEx().Rows)
            {
                cmbClub.Items.Add(dr[0].ToString());
            }
        }

        // when the user picks a club display it
        private void cmbClub_SelectedIndexChanged(object sender, EventArgs e)
        {
            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            // Query table
            con.SqlQuery("SELECT * FROM Clubs WHERE Clubname=@club_name");
            con.cmd.Parameters.AddWithValue("@club_name", cmbClub.SelectedItem);

            DataTable table = con.QueryEx();

            dgvClub.DataSource = table;
        }

        // When the user picks a cat display its clubs
        private void displaycat(string cat_name)
        {
            // Start a connect class
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Clubs WHERE Cat=@cat_name ORDER BY State, ClubName;");

            con.cmd.Parameters.AddWithValue("@cat_name", cat_name);

            DataTable table = con.QueryEx();
            dgvClub.DataSource = table;

            // Close Connection
            con.con.Close();
        }

        /*********************************************Radio Buttons********************************************/

        private void Art_CheckedChanged(object sender, EventArgs e)
        {
            showcat("ArtOrganization");
            displaycat("ArtOrganization");
        }

        private void Academic_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Academic");
            displaycat("Academic");
        }

        private void Sport_CheckedChanged(object sender, EventArgs e)
        {
            showcat("Sport");
            displaycat("Sport");
        }
    }
}
