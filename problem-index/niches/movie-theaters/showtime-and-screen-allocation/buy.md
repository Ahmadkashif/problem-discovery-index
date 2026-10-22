# Airline Schedule Optimisation for Auditoriums

**Niche:** [[niches/movie-theaters/showtime-and-screen-allocation/profile|Showtime & Screen Allocation]]
**Industry:** [[industries/movie-theaters|Movie Theaters]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Airlines assign aircraft of different sizes to departures under turnaround and crew constraints; theatres assign auditoriums to showtimes under the same kind of constraints, by hand.
**Tags:** #optimization-fundamentals #dynamic-programming #monte-carlo-methods #time-series-forecasting #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to forecast each film's next-week demand by theatre and daypart well enough to set screens and showtimes before the mid-week publishing deadline, and whoever gets the holdover calls right most often takes the account.

## The Problem
Building a 12-screen grid means fitting films of different lengths into auditoriums of different sizes, with cleaning turns between shows, staggered let-outs, premium formats, and peak demand concentrated in a few evening hours. Managers do it in the scheduling screen by trial and error.

## What Already Exists
Airline fleet-assignment and schedule-optimisation tools (Sabre, Lufthansa Systems, Google OR-Tools as a solver) match capacity to forecast demand under turnaround, crew and gate constraints.

## The Customization Gap
The adaptation needs: runtimes plus trailer reels as block times; cleaning turns that vary with seating type and attendance; crew capacity for simultaneous let-outs; distributor commitments on auditorium size and showtime count; daypart demand curves that shift by film audience; integration with Vista or Veezi to publish the grid; and a run time of seconds so it can re-optimise as presales move.

## Target Customer
Programming and operations teams at circuits running 8+ screen theatres.

## Impact If Solved
An optimised grid seats more of the forecast demand in the right-sized rooms and removes turn collisions, with the human retaining the final call.
