<h1>Student management system and data representing system</h1>
<h2>Overview:</h2>
  Here is the content of the Python code. 
  It takes input from the user to determine whether they are a "Student" or "Staff." Based on their choice, it either allows the user to calculate their progression as a student or handles a progression outcome recording system with a histogram for the staff. 
  The code also writes the results to a file (coursework scoring.txt) and draws a graphical histogram using the graphics module for staff.
<h3><b>1. </b>Staff ('t') version:</h3>
  Collects credits and calculates progression outcomes (Progress, Trailer, Exclude, Retriever).
  Displays results in a graphical histogram using graphics.
  Saves the results to a file and displays them.
<ul>
  <br>
  <li><b><h4>Progress:</h4> </b> The student has passed all modules with 120 credits and is allowed to progress to the next level.</li>
  <li><b><h4>Trailer:</h4> </b> The student has passed most modules (100 credits) and is trailing a small number of credits, allowing them to progress with conditions. </li>
  <li><b><h4>Exclude:</h4> </b>The student has failed 80 or more credits and is excluded from the course due to poor performance. </li>
  <li><b><h4>Retriever:</h4> </b>The student needs to retake or retrieve certain modules, as they haven't passed enough credits to progress but haven't been excluded. </li>
</ul>
<h3><b>2. </b>Student ('s') version:</h3>
  Similar progression calculation but without the graphical display and file handling.
<h2>Features of that program:</h2>
  <h3><b>1. Student and Staff Versions:</b></h3>
    <ul>
      <li>Students can calculate and display their progression outcomes.</li>
      <li>Staff can handle multiple students' data, visualize the outcomes in a graphical histogram, and save the data to a file.</li>
    </ul>
  <h3><b>2. Progression Outcome Calculation:</b></h3>
    <ul>
      <li>Calculates whether a student should "Progress," is a "Trailer," needs to "Retrieve" modules, or is "Excluded" based on their credit scores.</li>
    </ul>
  <h3><b>3. Data Validation:</b></h3>
    <ul>
      <li>Ensures that the sum of credits equals 120 and validates inputs to be within a predefined set of valid credit values (0, 20, 40, 60, 80, 100, 120).</li>
    </ul>
  <h3><b>4. Graphical Histogram (Staff Version):</b></h3>
    <ul>
      <li>Displays the count of each progression outcome (Progress, Trailer, Exclude, Retriever) as a bar chart using the graphics module.</li>
    </ul>
  <h3><b>5. File Handling:</b></h3>
    <ul>
      <li>Staff version saves the progression outcomes to a text file (coursework scoring.txt) and can later read and display the contents.</li>
    </ul>
  <h3><b>6. Data Persistence:</b></h3>
    <ul>
      <li>Allows staff to enter multiple sets of data and stores the results in a list, which is then saved and displayed.</li>
    </ul>
  <h3><b>7. Interactive User Interface:</b></h3>
    <ul>
      <li>Both versions allow the user to continue entering data or quit based on their input.</li>
    </ul>
<h2>Assumptions:</h2>
<ul>
  <li>The code assumes that you have the graphics module installed and set up to render graphics.</li>
  <li>The scoring file (coursework scoring.txt) will be created in the current working directory.</li>
</ul>
<hr><br>
This "README.md" file provides a comprehensive guide to your project, from installation and usage to contributing and licensing. 
Adjust the placeholders with specific details related to your project, such as the GitHub repository URL and any special acknowledgements. 
Let me know if you need further customization or additional sections!
