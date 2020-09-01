using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Diagnostics.Tracing;

namespace Club_GUI
{
    public partial class List_Activities : UserControl
    {
        public List_Activities()
        {
            InitializeComponent();
        }

        // Display Date and Time
        private void List_Activities_Load(object sender, EventArgs e)
        {
            // Clear the textbox
            rtbList.Clear();

            // Open connection
            Classes.SqlDBConnect con = new Classes.SqlDBConnect();

            con.SqlQuery("SELECT * FROM Activities ORDER BY Date DESC;");

            foreach (DataRow dr in con.QueryEx().Rows)
            {
                string activity = "__________\n" + dr["Date"].ToString() + "\n" +
                    dr["ClubName"] + "\n" + dr["cat"] + "\n\nActivity: " + dr["Club Activity"] +
                    "\n___________________________________________________________________________\n\n";

                rtbList.Text += activity;
            }

            // Close Connection
            con.con.Close();
        }
    }
}
