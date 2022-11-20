/*
 * this cpp file is used to generate random score in string format
 *
 * one single score as input, second-order markov chain
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
#define SCORE_LENGTH 80
// this is the name of the score you feed in, note that the suffix should be ".in"
// thus you will get a translate version of the input score, with the same name and a suffix ".out"
const string score_name = "mope";
// this is the name of the randomly spawn score, ".out" as its suffix
// this program will only use one single score as input and a second-order markov chain
const string rand_name = "mope_second_order";



// ! NO NEED TO MODIFY THE CODE BELOW

typedef std::pair<string, int> Note;
typedef std::pair<Note, Note> NotePair;

vector<Note> notes;
map<NotePair, vector<Note>> prob2;

int main()
{
    srand(time(0));

    ifstream infile;
    ofstream outfile;
    infile.open("./in/" + score_name + ".in", ios::in);
    outfile.open("./out/" + score_name + ".out", ios::out);
    if (!infile.is_open())
    {
        cout << "open failed." << endl;
        return 0;
    }

    string pitch;
    int duration;
    bool flag = false;

    outfile << score_name << " = (";
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

        Note note = make_pair(pitch, duration);
        flag = true;

        notes.push_back(note);
    }
    outfile << ")";

    infile.close();
    outfile.close();
    outfile.open("./rout/" + rand_name + ".out", ios::out);


    if (notes.size() < 3)
        return 0;
    for (int i = 2; i < notes.size(); i++)
    {
        prob2[make_pair(notes[i - 2], notes[i - 1])].push_back(notes[i]);
    }

    Note first = notes[0], second = notes[1];

    outfile << rand_name << " = (('" << first.first << "', " << first.second << "), ('" << second.first << "', " << second.second << ")";
    for (int i = 2; i < SCORE_LENGTH; i++)
    {
        auto pair = make_pair(first, second);
        if (prob2.find(pair) == prob2.end())
        {
            break;
        }

        auto p = prob2[pair];
        int j = rand() % (p.size());
        first = second;
        second = p[j];

        outfile << ", ('" << second.first << "', " << second.second << ")";
    }
    outfile << ")";

    outfile.close();
}