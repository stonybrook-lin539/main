---
title: Mathematical Methods in Linguistics
date: Fall 2024
---

| Course          | Info                                           |
| --:             | :--                                            |
| Course#         | LIN 361/539                                    |
| Time            | Mon/Wed 9:30-10:50am                           |
| Location        | SBS S-228                                      |
| Website         | lin361.thomasgraf.net (lecture notes)          |
|                 | lin539.thomasgraf.net (source code)            |
|                 |                                                |
| Instructor      | Thomas Graf                                    |
| Email           | [coursenumber]@thomasgraf.net                  |
| Drop-in hours   | Mon 11:00am-12:00pm                            |
|                 | Wed 2:30pm-3:30pm                              |
|                 | Fri 10:00am-11:00pm                            |
| Office          | SBS N-249                                      |
|                 |                                                |
| TA              | none `:(`                                      |


# Course Outline

## Bulletin Description

An overview of the mathematical foundations of theoretical and computational linguistics.
Topics covered include set theory, morphisms, logic and model theory, algebra, lattices, lambda calculus, probability theory, information theory, and basics of formal language theory.
A strong emphasis is put on the linguistic application of the mathematical concepts in the study and analysis of natural language data.


## Full Description

This course is an introduction to mathematics in linguistics.
It aims to help students familiarize themselves with mathematical concepts and applications that are widely relevant to theoretical and\slash or computational linguistics.
This covers a wide range of topics, mostly from *discrete mathematics*.
All the concepts will be illustrated with examples that have to do with natural language.
For linguistics students, this should make the math more approachable and engaging.
For mathematics students, this will show you a little-known but fascinating application area for mathematics.

The course is also very different from what you did in high school, there's precious few numbers here and we don't care much about trigonometry or calculating compound interest.
In contrast to a proper mathematics course, we also focus more on techniques and tools rather than theorems and proofs.
This means that you will learn how to work with things like functions, matrices, lattices, and finite-state automata, but you won't have to prove things about them.
So this is more like a CS methods course than a proper math class.

For more information about the content, consult the [Schedule](#Schedule).
You will see that the schedule for this class is very ambitious.
We probably won't be able to cover everything (I have taught this course many times, and I never made it all the way to the end).
But no matter how far we get, by the end of the class you should have had enough exposure to mathematical thinking that the thought of picking up a textbook in mathematics or computational linguistics for self-study won't make you run away in horror.

## Teaching Goals

- master essential concepts and techniques in mathematics and theoretical computer science
- apply mathematical techniques to the study of language
- formalize linguistic ideas in mathematical terms
- develop learning autonomy and the ability to expand your mathematical knowledge through self-study


## Prerequisites

No prior mathematical or computational experience is required.
We will get to see quite a bit of mathematical notation, like $(a \rightarrow \neg a) \rightarrow \neg a$ or $$\begin{pmatrix} 1 & 0\\0 & 0\\\end{pmatrix} \otimes \begin{pmatrix} 0 & 0\\1 & 1\end{pmatrix}$$ 
But you don't need to know yet what any of that means.

There's no linguistic prereqs either, but since I'm a linguist I might sometimes forget what parts of linguistics are not common knowledge.
Don't feel shy to ask clarification questions.
Anecdotal evidence: I have run this course as an independent study with high school students who had no prior experience in linguistics, and they could follow along just fine because they were not afraid to ask me to clarify some linguistic concepts.


## Textbook

None, but there are detailed lecture notes that I am trying to turn into a textbook.
The lecture notes are shared as a website: <http://lin361.thomasgraf.net>

# Schedule

As usual, this schedule represents the ideal scenario.
In the real world, we probably won't get to cover all of this.

| Wk  | Date     | Topic                                    | Assignment                     |
| :-- | :--      | :--                                      | :--                            |
| 1   | M 08/26  | On-boarding                              |                                |
|     |          |                                          |                                |
|     |          | **Block 1: N-gram grammar**              |                                |
| 1   | W 08/28  | N-gram grammars for phonotactics         | Pre-assessment                 |
| 2   | M 09/02  | no class (Labor day)                     |                                |
| 2   | W 09/04  | N-gram grammars more formally            | Homework (P/F graded)          |
| 3   | M 09/09  | Translating between grammars             |                                |
| 3   | W 09/11  | Adding phonological tiers                | Homework (P/F graded)          |
| 4   | M 09/16  | N-gram grammar odds and ends             |                                |
| 4   | W 09/18  | Q\&A and recap                           | Take-home exam (letter graded) |
|     |          |                                          |                                |
|     |          | **Block 2: Universals and monotonicity** |                                |
| 5   | M 09/23  | The \*ABA generalization                 |                                |
| 5   | W 09/25  | \*ABA continued                          | Homework (P/F graded)          |
| 6   | M 09/30  | Negative polarity items                  |                                |
| 6   | W 10/02  | Case syncretism                          | Homework (P/F graded)          |
| 7   | M 10/07  | Person Case constraints                  |                                |
| 7   | W 10/09  | Universals for learning                  | Homework (P/F graded)          |
| 8   | M 10/14  | no class (Fall break)                    |                                |
| 8   | W 10/16  | Q\&A and recap                           | Take-home exam (letter graded) |
|     |          |                                          |                                |
|     |          | **Block 3: Underlying representations**  |                                |
| 9   | M 10/21  | Why n-grams don't work for mappings      |                                |
| 9   | W 10/23  | Finite-state transducers                 | Homework (P/F graded)          |
| 10  | M 10/28  | Transducers for phonology                |                                |
| 10  | W 10/30  | Capturing rule ordering                  | Homework (P/F graded)          |
| 11  | M 11/04  | Phonological parsing                     |                                |
| 11  | W 11/06  | Generative capacity of FSTs              | Homework (P/F graded)          |
| 12  | M 11/11  | Strictly local transductions             |                                |
| 12  | W 11/13  | Two-level morphology                     | Homework (P/F graded)          |
| 13  | M 11/18  | FSAs as Boolean matrix multiplication    |                                |
| 13  | W 11/20  | Q\&A and recap                           | Take-home exam (letter graded) |
| 14  | M 11/25  | final recap                              |                                |
| 14  | W 11/27  | no classes (Thanksgiving break)          |                                |
|     |          |                                          |                                |
|     |          | **Block 4: Let's have fun**              |                                |
| 15  | M 12/02  | Topic of your choice (e.g.               |                                |
| 15  | W 12/04  | neural networks, sentence processing,    |                                |
| 16  | M 12/09  | logic for linguistics)                   | Post-assessment                |

And here's a list of mathematical concepts we will master in the process:

- sets
- strings
- multisets
- tuples
- functions
- monotonicity
- relations
- orders (partial, total, weak, strict)
- posets
- (semi)lattices (meet, join)
- linear algebra (vectors, dot product, matrix multiplication; possibly tensor products)
- and depending on what fun topics we choose at the end:
    - graphs (connectedness, components)
    - antimatroids, with applications to OT
    - propositional & first-order logic
    - type theory
    - lambda calculus
    - information theory (entropy, cross-entropy, surprisal)

# Grading

## Undergraduate students

By default, 100% of your grade are determined by a **final exam (taken in person)**.
But there are various things you can do throughout the semester to reduce the importance of the final exam.
This way, students who would rather study on their own can just do that and get their grade by demonstrating their knowledge on the final exam.
Students who participate more regularly instead get to minimize the risk that a bad final exam will ruin their grade.

1.  **Class participation (10%)**  
    Show up all the time, ask questions and participate in discussion, and you will get an A for class participation.
    That A makes up 10% of your grade.
    If you do not meet this standard of active participation, this component is ignored for calculating your final grade.

1.  **Pre-assessment (P/F; 5%)**  
    At the beginning of the semester, students are asked to take a survey to assess their prior knowledge of mathematical linguistics.
    It is perfectly normal not to know a single answer.
    Performance is P/F depending on whether a filled-out survey was submitted (answering "Don't know" on each question is perfectly fine).
    If you get a P, that is treated like an A and is worth 5% of your grade.
    If you get an F or do not hand in the pre-assessment, this component is ignored for calculating your final grade.

1.  **Post-assessment (P/F; 5%)**  
    Exactly the same as the pre-assessment.
    Just do it again and pat yourself on the shoulder for every question you now know the answer to.
    If you get a P, that is treated like an A and is worth 5% of your grade.
    If you get an F or do not hand in the pre-assessment, this component is ignored for calculating your final grade.

1.  **Weekly assignments (P/F; 20% total)**  
    A list of exercises from the lecture notes is assigned every Wednesday and your answers are due a week later in class.
    You should make a reasonable effort to complete the exercises, but your answers are not really graded.
    As long as it is clear that you made an effort, you get a P, which is treated as an A. 
    There will be approximately 8 to 10 assignments, so each assignment is worth somewhere between 2% to 2.5% of your grade.
    If you get an F or do not hand in the assignment, that is ignored for calculating your final grade.
    Full solutions for each assignment will be distributed shortly after the assignment is collected.

1.  **Three take-home exams (A-F; 20% each)**  
    Take-home exams are longer than regular assignments and are letter graded.
    The grade on a take-home exam counts only if it is higher than the grade on the final exam, otherwise we ignore it.
    The reasoning behind that is that if you bomb a take-home exam but then shape up and turn in a great final exam, that's something to be rewarded, not punished.
    Full solutions for each take-home exam will be distributed shortly after the exams are collected.

Another way to look at this: if you do all the things above and do well on them, then you don't need to come to the final exam!

The final grade is calculated by converting grades to points weighted by the respective percentages.

| Grade | Point scale |
| :--   | --:         |
| A     | 10.0        |
| A-    | 9.5         |
| B+    | 9.0         |
| B     | 8.5         |
| B-    | 8.0         |
| C+    | 7.5         |
| C     | 7.0         |
| C-    | 6.5         |
| D+    | 6.0         |
| D     | 5.5         |
| F     | 5.0         |

*Example 1*:
Alan Turing decides that he doesn't want to do any work during the semester and instead puts everything on one card by taking only the final exam.
He gets an A-, and thus his grade in the course is also A-.

*Example 2*:
Ada Lovelace is a very active participant in class (10% A), has handed in both the pre-assessment (5% A) and the post-assessment (5% A), got a P on 9 out of 10 assignments (18% A), and an A- on every take-home exam (60% A-).
She decides to entirely skip the final exam (grade F).
Her total grade is $.38 * 10.0 + .6 * 9.5 + .02 * 5.0 = 9.6$, which is just barely enough for an A.

*Example 3*:
Hal 9000 is having a rough semester.
He handed in the pre-assessment (5% A) but not the post-assessment.
He also handed in 5 out 10 assignments, but only 4 got a P (8% A).
He got an A- on the first take-home exam (20% A-), a C on the second take-home exam (20% C), and didn't hand in the third take-home exam.
The final exam went fairly well and he got a B+, which means that the C on the second take-home exam doesn't factor into the final grade.
His total grade is $.05 * 10.0 + .08 * 10.0 + .2 * 9.5 + .67 * 9.0 = 9.231$, which is an A-.


## Graduate students

The grading is the same as for undergrads, except that:

1.  The weekly assignments may contain exercises that are optional for undergrads but mandatory for grads.

1.  Once during the semester, you have to serve as pseudo-grader.
    You will get to look at the assignments, then you will meet with me to discuss what you think the students did well, what they struggled with, and who (if anybody) you think should not get a P due to lack of effort.

## Student pseudonyms

Because the grad students in this course will get to look at the handed-in assignments, we will put in place an extra measure to protect your privacy.
At the beginning of the semester, you will pick a pseudonym, and whenever you hand in an assignment, you will use that pseudonym instead of your real name.
Detailed instructions will be sent out in a separate announcement.

## Late hand-ins

There isn't much wiggle room for late hand-ins because the solutions for all assignments and take-home exams are distributed shortly after the assignments are collected (usually within 24 hours).
But keep in mind that these assignments are optional, so missing one or two isn't the end of the world.

## ChatGPT

You are allowed to use ChatGPT for assignments and the take-home exams, but if you do so, please indicate that you did.
It won't matter for grading or anything else, but I would like to know whether students actually benefit from using ChatGPT.
Here is some advice based on my own experimentation:

1. Do not blindly copy-paste answers from ChatGPT.
   Treat it like a discussion with a peer, be aware that said peer may well be wrong, then write up your own answer.

1. ChatGPT will often get things wrong, in particular on the exercises that combine math and linguistics.
   But it can be insightful to think about what it got wrong, and why.
   Contrast what ChatGPT does against the official solutions for exercises, and you may have quite a few epiphanies.

1. Use ChatGPT selectively.
   It can take a lot of time to convert an exercise into a prompt that ChatGPT can do something with.
   It's often faster to just do things by yourself.
   Use ChatGPT for the exercises that really have you stymied, the exercises where you don't even know how to get started.

## A remark on grades

Yes, this class has a grading system that is easy to game.
You could just use ChatGPT to do the weekly assignments and take-home exams and then opt out of the final exam.
But that means you'll have paid the university a decent sum of money on a course that you learnt nothing from.
If you're okay with that, then I'm okay with that, just like your gym doesn't mind that you pay them fifty bucks a month but never show up.

My experience is that the students who shouldn't get a good grade somehow manage to get a low grade even under the most lenient grading system.
No reason to tighten clamps that will only make things more annoying for students who do just fine without all those extra hoops to jump through.


# Policies

## Contacting me

- Emails should be sent to [coursenumber]@thomasgraf.net.
  Disregarding this policy means late replies and might easily make me cross.
- Reply time < 24h in simple cases, possibly more if meddling with bureaucracy is involved.
- If you want to come to my office hours and anticipate a longer meeting, please email me so that we can set apart enough time and avoid collisions with other students.

## Student Accessibility Support Center Statement

If you have a physical, psychological, medical, or learning disability that may impact your course work, please contact the Student Accessibility Support Center, Stony Brook Union Suite 107, (631) 632-6748, or at <sasc@stonybrook.edu>.
They will determine with you what accommodations are necessary and appropriate.
All information and documentation is confidential.

Students who require assistance during emergency evacuation are encouraged to discuss their needs with their professors and the Student Accessibility Support Center.
For procedures and information go to the following website:
<https://ehs.stonybrook.edu//programs/fire-safety/emergency-evacuation/evacuation-guide-disabilities> 
and search Fire Safety and Evacuation and Disabilities.

## Academic Integrity Statement

Each student must pursue his or her academic goals honestly and be personally accountable for all submitted work.
Representing another person's work as your own is always wrong.
Faculty is required to report any suspected instances of academic dishonesty to the Academic Judiciary.
Faculty in the Health Sciences Center (School of Health Technology & Management, Nursing, Social Welfare, Dental Medicine) and School of Medicine are required to follow their school-specific procedures.
For more comprehensive information on academic integrity, including categories of academic dishonesty please refer to the academic judiciary website at
<http://www.stonybrook.edu/commcms/academic_integrity/index.html>

## Critical Incident Management

Stony Brook University expects students to respect the rights, privileges, and property of other people.
Faculty are required to report to the Office of Student Conduct and Community Standards any disruptive behavior that interrupts their ability to teach, compromises the safety of the learning environment, or inhibits students' ability to learn.
Until/unless the latest COVID guidance is explicitly amended by SBU, during Fall 2021 "disruptive behavior” will include refusal to wear a mask during classes.  

For the latest COVID guidance, please refer to: <https://www.stonybrook.edu/commcms/strongertogether/latest.php>
