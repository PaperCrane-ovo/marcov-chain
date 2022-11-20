/*
 * this cpp file is used to generate random score in string format
 *
 * two scores as input, first-order markov chain
 * take both pitch and duration into consideration
 *
 * put your input score into "in" directory, you will get a translate version
 * of the score in "out" directory, and a randomized version in "rout" directory
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <ctime>
using namespace std;

// ! MODIFY THIS PART

// the length of the randomly spawn score, should be an int greater than zero
#define SCORE_LENGTH 200
// these are the names of the score you feed in, note that the suffix should be ".in"
// thus you will get a translate version of the input score, with the same name and a suffix ".out"
const string first_score_name = "sunny";
const string second_score_name = "road";
// this is the name of the randomly spawn score, ".out" as its suffix
// this program will only use one single score as input and a first-order markov chain
const string rand_name = "sunny_road_first_order";



// ! NO NEED TO MODIFY THE CODE BELOW

typedef std::pair<string, int> Note;
map<Note, vector<Note>> prob;
Note start_note;

int translate(const string& name)
{
    ifstream infile;
    ofstream outfile;

    infile.open("./in/" + name + ".in", ios::in);
    outfile.open("./out/" + name + ".out", ios::out);

    if (!infile.is_open())
    {
        cout << "open failed." << endl;
        return -1;
    }

    string pitch;
    int duration;
    bool flag = false;
    Note pre_note;

    outfile << name << " = (";
    while (infile >> pitch >> duration)
    {
        if (flag) outfile << ", ";
        //cout << note << " " << duration << endl;
        outfile << "('" << pitch << "', " << duration << ")";

        int len = pitch.length();
        if (pitch[0] >= 'A' && pitch[0] <= 'Z')
            pitch[0] -= ('A' - 'a');
        if (pitch[len - 1] < '0' || pitch[len - 1] > '9' && pitch[0] != 'r')
            pitch = pitch + "4";

        Note note = std::make_pair(pitch, duration);
        if (flag)
        {
            prob[note].push_back(pre_note);
        }
        else
        {
            start_note = note;
        }

        pre_note = note;

        flag = true;
    }
    outfile << ")";

    infile.close();
    outfile.close();

    return 0;
}

int main()
{
    srand(time(0));

    if (translate(first_score_name) < 0)
        return 0;
    if (translate(second_score_name) < 0)
        return 0;

    ofstream outfile;
    outfile.open("./rout/" + rand_name + ".out", ios::out);

    Note cur = start_note;

    outfile << rand_name << " = (('" << cur.first << "', " << cur.second << ")";
    for (int i = 1; i < SCORE_LENGTH; i++)
    {
        if (prob.find(cur) == prob.end())
        {
            break;
        }

        auto p = prob[cur];
        int j = rand() % (p.size());
        cur = p[j];

        outfile << ", ('" << cur.first << "', " << cur.second << ")";
    }
    outfile << ")";
    outfile.close();
}