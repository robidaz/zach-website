--- Page 1 ---
Robida, Zachary 2019 Year-End
Consultant Organization:(inactive)
Manager:Michaela McGinty Location: Atlanta
Evaluated By:Michaela McGinty 01/01/2019 - 12/31/2019
Overall Rating
Manager Overall Evaluation
Rating: Role Model (5)
Employee Overall Evaluation
Rating: Role Model (5)
Acknowledgement
Manager
Entered by: Michaela McGinty Date: 01/28/2020
Status: Manager Acknowledgement
Comment: Completed MPOWER and compensation review with Zach.
Employee
Entered by: Zach Robida Date: 01/29/2020
Status: Employee Acknowledgement
Comment:
Priorities
Contribute to the security documentation, security software build out and configuration, testing, and
cloud operations processes.
Due Date: 12/31/2019 Status: Successfully Completion Date:
complete
Category:
Organization Alignment:
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Comment: Zach quickly became a core contributor in the Comment: During the preliminary phase of developing
cloud migration project and took initiative to the ManhGov Cloud system, our department
lead several critical areas of the project such was focused on ensuring that our system
as WebInspect scanning, Windows was going to meet all necessary FedRAMP
hardening, PowerShell scripting, Vulnerability controls so that we could be given Authority
remediation, and automated testing. His to Operate. I was given the opportunity to
ability to pick up technical skills quickly was play a large role in ensuring our cloud
critical to our success this year in building out solution met all the required controls in the
a FedRAMP High compliant environment, continuous monitoring facet; my center of
having our security documentation in order, focus was dedicated to Dynamic Application
and getting FEMA live in the cloud. Zach was Security Testing (DAST). Due to the nature of

--- Page 2 ---
also able to onboard others to the many our resource distribution I was responsible for
areas he was involved in and was great at both the technical and functional aspects of
delegating tasks to newer consultants / co- building our DAST component. One major
ops so they could contribute as well. Zach’s hurdle that had to be overcome was the fact
work this year on the cloud project has laid that all of developers at my disposal were
the foundation for much of our cloud primarily experienced in deploying enterprise
operations processes, security software to unix based systems, however the
documentation, vulnerability management, DAST tool we had chosen, Webinspect, was
and continuous improvement mindset. only supported by windows operating system.
This meant that on top of the application
security related knowledge I was tasked with
learning (which I will elaborate on in a later
paragraph), I also had to become
knowledgeable in the practice of securely
deploying and installing enterprise software
on window servers. During the course of the
project I became the pioneer for the majority
of all windows related cloud operation
procedures including but not limited to:
· Securely transferring files from
Amazon’s S3 bucket to windows servers
· Performing crucial windows updates
that if left unpatched would have left potential
critical vulnerabilities open
· Installing agents on all windows
servers to ensure that they could be properly
scanned by our advanced vulnerability
scanner Nessus
· Developing a process for hardening all
windows servers with a GPO (group policy
objects) I created manually to align our
server configuration with the most recent
DISA STIG (Security Technical
Implementation Guide administered by the
Defense Information Systems Agency) so
that our systems were secure and abided by
FedRAMP controls
· Writing the first version of a script
which performed all additional hardening
tasks such as renaming the host to its proper
DNS, syncing the server with our NTP serves
(network time protocol) and installing
required dependencies and agents
Once the majority of the server preparation
was complete, I was primarily focused on
installing WebInspect and configuring the
application to scan our own LSCMS and TP
applications. Due to the fact that no
application is the same across the board, the
base WebInspect scanning policies had to be
configured to detect vulnerabilities that were
relevant to our own software. In order to
make this happen I had to learn about the

--- Page 3 ---
Seven Pernicious Kingdoms, which is the
taxonomy which categorizes specific
vulnerabilities into larger security flaw
classes. Once I became familiar with the
terms, I also had to learn which frameworks
our applications were built on so that I could
configure the scan to target specific potential
vulnerabilities and limit scan duration.
Additionally, I had to review all of our initial
findings and collaborate with developers and
outside consultants to determine how to
provide certain parameters that would
eliminate true false positives without
overlooking real potential vulnerabilities.
Once I had successfully determined the ideal
configuration settings for WebInspect I
recognized a need to include all scanning
based activity into a rigid automated process
which could be streamlined directly into our
continuous monitoring as part of our normal
cloud operations process. To satisfy this
need I designed and partially developed a
fully integrated, autonomous vulnerability
detection and reporting framework ( which I
will elaborate on further in Goal #3).
By the time we were ready to be evaluated I
had successfully set up a working DAST
system, started a process for autonomously
scanning our applications, and created a
process for hardening windows servers. I
demonstrated my ability to merge my
business and technical skills by drafting a
generous portion of our continuous
monitoring SOP, documenting scanning
configuration baselines, and creating multiple
QRGs as part of an effort to disseminate all
of the technical information I had learned.
Elevate my understanding of the FEMA business process such that I can contribute to the
requirements gathering and design of new functionality for LSCMS
Due Date: 12/31/2019 Status: Successfully Completion Date:
complete
Category:
Organization Alignment:
Manager Evaluation Employee Evaluation
Rating: Successful Contributor (3) Rating: Successful Contributor (3)
Comment: The majority of Zach's time this year was Comment: As with a majority of people in our
spent on the cloud project and automated department, a great deal of my time was
testing. As such, he didn't have many spent on the Manhgov Cloud and improving

--- Page 4 ---
opportunities to contribute to the testing procedures. However more recently I
requirements gathering and design for the was given the opportunity to expand my
FEMA solution. However, during the summer knowledge in the actual FEMA business
and fall, Zach led the automated testing process by starting to get involved in our
keyword build-out and organize them into a transportation procurement system, the WM
regression test script for the application. Zach upgrade, and DISC-SAMs interface change
sought guidance from more experienced requests. During this process I have gotten to
consultants on FEMA processes to ensure work with people far more experienced than
the keywords and regression test script myself in relation to how our team has
appropriately reflected the FEMA business configured and customized our software to
processes. meet FEMA's needs. While it is true to say
that I have significantly elevated my
understanding of the FEMA business process
and contributed to requirements gathering, I
recognize that I have much to learn and look
forward to getting to a place where I can
successfully take on a role where I can be
the lead in designing a new functionality for
LSCMS.
Identify areas of improvement for internal processes and help create/implement new strategies that
allow our department to run more efficiently.
Due Date: 12/31/2019 Status: In progress Completion Date:
Category:
Organization Alignment:
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Comment: Zach continues to an ability to identify, Comment: One of the primary reasons I became an
design, and implement opportunities for engineer was so that I could exercise my
efficiency in all aspects of our department passion for identifying problems and working
and projects. A few notable examples include: to provide quality solutions. After deciding on
• Designing, developing, and overseeing a career path of a supply-chain software
the development of our vulnerability consultant, I was unsure that I would get the
detection and reporting framework. The opportunity to practice technical based
vulnerability automation has saved us problem solving. As it turned out I made a
hundreds of hours of pouring over great choice and in my 1.5 years at
vulnerability reports, manually analyzing Manhattan Associates I have been given
the results, and manually uploading endless opportunities and an abundance of
tickets into Jira. Without this project, our trust from management to identify sources of
department would have been much more inefficiency or areas that could use
disorganized regarding our vulnerability improvement and dedicate my time to
scanning and management. developing solutions.
• Developing parallel-execution of
WebInspect scans, which used to be run One example of a solution I designed and
individually and take many hours. The partially developed was a fully integrated,
scans can now be kicked off easily by a autonomous vulnerability detection and
scanning administrator and complete in reporting framework. Without any innovation
much less time. the Manhgov cloud DAST facet would be
nearly fully manual. A scanning admin would

--- Page 5 ---
• Designing and Developing the Manh- have had to manually kick off each individual
Robo automating testing framework. scan, export results, cross-reference each
Zach has spent a large portion of his discovered vulnerability to what is in service
time on the manh-robo project - a new desk and find a way to store the data in
automated testing framework. This AT compliance with the FedRAMP controls on
framework saves hundreds of hours of long-term vulnerability tracking. The solution I
manual testing time and allows our team designed allows 2 scans to be run in parallel
to do consistent thorough testing. Zach while working off a queue of all required scan
has taken the lead on this project and targets, auto-exports them in the desired/
has developed/designed many required formats, securely uploads them to
improvements along the way. His work our Amazon S3 bucket, creates new tickets
has helped our department run more in servicedesk, and parses the raw data and
efficiently and will lay the ground work inserts records into Amazon's Athena for
for future consultants and projects permanent storage. Additionally once the
utilizing automated testing. data has been uploaded to Athena
specialized views can be created to display
interesting data as well as used to
autogenerate our POA&M and create
monthly continuous-monitoring reports. After
designing this solution I developed around
60% of it until I moved my focus to another
project, at which point I became a major
overseer and assisted the consultants
working to finish the project.
Another major contribution I made to process
improvement was developing a brand new
custom automated-testing framework based
on a framework that the MATS team had
created. I noticed many problems with the
legacy framework that severely limited a
consulant's ability to effectively test our
application. The legacy framework had many
technical limitations such as speed,
unexpected failures, deprecated/unsupported
languages, and poor test execution methods.
Additionally the framework was not
conducive to consultants for creating test
cases for unique situations. These problems I
experienced as a personal user of the
framework and also knowledge of an
impending need to do regression testing on a
monthly basis inspired me to create a better
solution. Along with the help of several
contributors, I developed Manhrobo, a
lightweight, portable solution with the primary
design goal of empowering consultant's
ability to test effectively and efficiently.
Manhrobo has effectively replaced roughly
80% of consultant based testing. Prior to
automated testing a full regression test would
have taken 6 consultants a full week to
complete, a time frame which is not feasible

--- Page 6 ---
when factoring in a need to test monthly, in
multiple environments, with limited consulting
resources. With Manhrobo tests can be run in
any environment in a span of 30 minutes.
Additionally all forms of human error that
could otherwise be introduced at test time are
removed and logs and reports are
automatically generated. Testing with
Manhrobo also greatly increases the chances
of finding more obscure errors by
randomizing input test data and catching
errors that only happen on random occasions.
Increase the depth of my functional understanding of the Manhattan solutions used by FEMA
Due Date: 12/31/2019 Status: Successfully Completion Date:
complete
Category:
Organization Alignment:
Manager Evaluation Employee Evaluation
Rating: Performance Leader (4) Rating: Performance Leader (4)
Comment: Zach has had opportunities this year to Comment: One major benefit of working on the
become very familiar with the functionality automated-testing project was that all of the
and use cases of the FEMA solution as a regression tests had to be ported over or
whole and the individual applications created a first time. An important part of any
themselves. With leading the WebInspect testing is determining what the expected
vulnerability scanning, he had to become results are given a specific of parameters and
technically familiar with the architecture, actions. In order to develop effective tests,
networking, and scanning process of our web we had to determine what conditions resulted
applications. Zach also led the development in a categorizing as a pass vs fail. This
of the automated testing keywords, which means that I while created keywords I had to
required a general understanding of the learn what every possible field was that could
Manhattan solutions, how they're used by be filled out and determine if the expected
FEMA, how they work on in the background, outcome differed based on the parameter
and how they work together. Zach had to be that was provided. Over the course of the
able to understand the FEMA solution such year I played a major role in developing test
that he could develop the logic for the cases and forming the logic which
keywords and how to accurately test the determines what checks and validations are
solution using these keywords across all done at each test step to ensure that proper
facets of the FEMA solution. testing is being conducted. Over the course
of the year I either created or assisted in
creating keywords and test cases ( of
differing length and complexity) which
spanned our EEM, TPE, WM, AM, and DISC
modules.
Mentor and transfer knowledge to newer consultants and co-ops on software design principles,

--- Page 7 ---
automated testing, the ManhGov Cloud project, and the LSCMS solution in order to raise the overall
team skill-level.
Due Date: 12/31/2019 Status: In progress Completion Date:
Category:
Organization Alignment:
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Comment: Zach stepped in quickly to train and mentor Comment: When I first started, one thing I admired
Shaazan, Isabelle, and Aaron this year. He about our department was most people's
coordinated their new-hire training and willingness to assist me with learning new
onboarded them to various tools such as information and skills. I recognize that the
Automated Testing, AWS, Python, and most efficient way to get work is not to do it
Windows PowerShell scripting. He was able all yourself, but to train and mentor
to give them tasks, advise on their work, and employees to a point where they can produce
help them prioritize across several ongoing the same work and provide an additional
projects all throughout the year. Zach's point of view. Because of this I made it my
initiative and leadership in helping manage goal to be an open door for all new
the newer consultants and co-ops was crucial employees in our department to ask
during this busy year and cannot be questions and bounce ideas off. I also made
understated. sure to carefully provide constructive criticism
and suggest advice when needed if I saw
room for improvement or a potential better
solution. One way I did this was introduce
and encourage our new consultants to learn
or increase knowledge of Python so that they
could increase technical acumen and be
better equipped when it came to solving
problems. Having learned to code on my own
I was aware of the troubles of learning
something new and complex and I
communicated to all new consultants that if
they were unable to figure something out
after a short period of time that they could
ask me any questions no matter how trivial.
One of the best opportunities I got this year
was to be a "buddy" to our co-op Isabelle.
Despite the fact that I was not her actual
manager, I was able to spend a great deal of
time mentoring her and encouraging her to
increase her problem solving abilities through
technical innovation while she helped to
expand our automated-testing suite. I also
got invaluable managerial experience
through delegating work to her in a way that
was enjoyable and fulfilling to her. At the start
of her second term we had a recap meeting
of everything she had accomplished in her
first term and I asked her what she wanted to
work on because I ensured her that I wanted

--- Page 8 ---
to make that happen. While she continued to
provide outstanding work for automated
testing, I was also able to find an outlet for
her to contribute to our ManhGov cloud by
giving her a project that would allow her to
apply what she had learned in her SQL class
over the summer by developing our
vulnerability database in Amazon's Athena.
Having a goal to mentor was crucial to my
own personal development and I look forward
to continuing to mentor new employees so
that everyone (including myself) can continue
to evolve and become better suited to work
on our ever-growing ManhGov cloud solution.
Competencies
Collaboration
Working effectively and cooperatively with others; establishing and maintaining good working relationships across teams
and geographies.
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Communication
Clearly conveying information and ideas both in writing and orally to individuals or groups in a manner that engages the
audience and helps them understand and retain the message.
Manager Evaluation Employee Evaluation
Rating: Successful Contributor (3) Rating: Successful Contributor (3)
Customer Focus
Ensuring the customer (internal and external) is at the center of everything we do and that their perspective is a driving
force behind business decisions and activities; crafting and implementing service practices that meet customers' and own
organization's needs.
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Initiative
Taking prompt action to accomplish work goals; taking action to achieve results beyond what is required; being proactive.
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Planning and Organizing
Establishing a results focused action plan for self to complete work efficiently and on time by setting priorities, establishing
timelines, and leveraging resources.
Manager Evaluation Employee Evaluation
Rating: Performance Leader (4) Rating: Performance Leader (4)

--- Page 9 ---
Technical/Professional Acumen
Having achieved a satisfactory level of technical and professional skill or knowledge in position-related areas; keeping up
with current developments and trends in areas of expertise.
Manager Evaluation Employee Evaluation
Rating: Role Model (5) Rating: Role Model (5)
Section Summary
Manager Evaluation Employee Evaluation
Comment: • Zach has continued to grow in many Comment: Collaboration – This year I believe I took
areas of his professional and technical advantage of every opportunity to collaborate
development. He has proven that he can that I was presented with or came across.
work on some of the most challenging After being heavily involved in the continuous-
tasks and master them as quickly as monitoring facet of the gov cloud I was
anyone. He has continued to show some constantly working with other consultants and
of the best initiative I've seen at our C.A.B to ensure that all aspects of
Manhattan; if he sees something that FedRAMP compliance were being
needs to be done that's even remotely acknowledged, tracked, and ultimately met.
related to what he's working on, he'll take Additionally I became a quasi-technical
the lead and do it. Zach has proven to analyst when resources were low and spent a
work well in all areas of our department lot of time working to solve technical problems
and with all members of our department. with analysts in order to work towards an end
Zach has also frequently sacrificed time goal of standing up a working and compliant
outside of work to ensure we meet critical DAST system. I also led all automated-testing
client project deadlines. The cloud project efforts, managing the contributions of up to 4
would not have been anywhere near the other consultants to further innovate the
success it was without his determination solution. Lastly I demonstrated my ability to be
and sacrifice. a variable resource, meaning that after
• Zach should look to capitalize on the starting the WebInspect Automation project I
upcoming projects in the government successfully transferred my knowledge to
department to develop a deeper another consultant and oversaw the project
understanding of the Manhattan from afar while my efforts were shifted to other
applications, software design, and the projects at the request of management.
client. Additionally, he will have
opportunities to hone his communication Communication – Some of the constructive
skills in a variety of ways such as internal criticism I received earlier in the year was that
communication, client communication, I struggled to provide quality status updates.
project status communication, and After being given several very valid examples I
technical communication. As Zach made an effort to restructure my updates so
transitions into a lead consultant, his that I transferred only absolutely necessary
ability to communicate to his colleagues information to the proper audience.
at all levels and background will become Additionally I was the primary point of contact
critically important. for consultation with Saltworks Security,
• Zach has had a fantastic second year at vulnerability reporting with IBM, and
Manhattan and continues to prove himself Webinspect problem reporting and service
as a model PSO consultant with his requests with Microfocus Fortify as needed. I
technical skills, ability to learn anything also worked to provide upwards
handed to him, and initiative to get things communication to management when I
done. identified potential flaws/gaps in our testing
processes so that we could allot consultant
time to audit our test criteria as well the
breadth and depth of each test scenario.
While I truly believe that my communication

--- Page 10 ---
skills grew in response to the feedback, I
received I rated myself a 3 because I
recognize that there are other areas that I can
continue to improve upon by increasing my
communication frequency and taking trainings.
Customer Focus – One way I worked to
ensure custom focus was working late hours
and long days to progress with AT
development (to ensure that the system
owner would feel satisfied with breadth/depth
of testing during patch cycles and free-up
functional resources). I hit every deadline
needed to present results to FEMA on time
and proceed with our patch cycle. I also
worked hard to ensure that WebInspect scans
were conducted and that I provided clear and
accurate scan results in the formats that the
clients desired.
Initiative – Refer to goal: Identify areas of
improvement for internal processes and help
create/implement new strategies that allow our
department to run more efficiently.
Planning and Organizing – As I also
mentioned in the Collaboration section I was
the automated testing “project manager” for
which I managed the contributions of 4 other
consultants. I worked carefully to divide up all
open tasks and future improvements into
pieces such that for each new major test run
the framework was in a working state of
continuous improvement. I also was the
overseer of the WebInspect Automation
project for which I divided into 7 phases for
which each phase was an additionally
functionality that would not affect the usability
of prior phases work.
Technical/Professional Acumen
-Became an advanced user of Python which I
used to develop ManhRobo and the
WebInspect Automation on. I learned how to
utilize object-oriented programming to
compartmentalize various aspects of
ManhRobo so that future changes to our
applications would only require a small
number of modules to be adapted rather than
rework the whole framework.
-Learned about TLS protocol and other areas
of network infrastructure so that I could
effectivley contribute to the application
vulnerability remediation process
-Became knowledgeable of many AWS Cloud

--- Page 11 ---
Computing services (Windows EC2, S3,
Athena)
-Demonstrated mastery of beginner/
intermediate SQL concepts by teaching a
class to new hires
Enter Development Items
Customer Focus
Additional Information: Now that I have been badged I am looking forward to expanding my customer focus audience to
FEMA
Status: Not Started
Communication
Additional Information: I would like to successfully disseminate information relating to automated testing to all
consultants, eventually outside of our department. I also want to work on my intradepartmental
skills by working to increase the frequency in which I update my superiors on the status of my
work. I also think I benefit greatly from taking the Better Business Writing course and pledge to
do so in the year 2020.
Status: In Progress