library(shiny)
library(shinyWidgets)
library(tidyverse)
library(dplyr)
library(geometry)

# Define UI for application that draws a histogram
ui <- fluidPage(
  #CSS
  tags$head(
    tags$style(HTML("hr {border-top: 1px solid #000000;}"))
  ),

  #Setting Background Color
  setBackgroundColor(color = "MintCream"),

  # Application title
  titlePanel("PH 142 Grade Estimator"),

  hr(),
  fluidRow(
    column(12,
           HTML("<b>For the course's overall grade distribution, please see the syllabus on the course website.<br><br> Lab </b><br/> Select 'Completed' or 'Not Completed' for each lab or 'Unknown' for future labs. </br> 
                <br>Lab 11 can optionally be completed in replacement of your lowest lab score <i>(for a total of 9 graded lab submissions).</i><br/> 
                <b>One 'Not Completed' lab will automatically be dropped. </b><br/><br/>")),
    column(2,
           radioButtons("lab01", "Lab 01", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab02", "Lab 02", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab03", "Lab 03", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab04", "Lab 04", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab05", "Lab 05", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown"))),
  fluidRow(
    column(2,
           radioButtons("lab06", "Lab 06", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab07", "Lab 07", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab08", "Lab 08", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab09", "Lab 09", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab10", "Lab 10", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown")),
    column(2,
           radioButtons("lab11", "Lab 11 (optional)", choices = c("Completed", "Not Completed", "Unknown"), selected = "Unknown"))),
  fluidRow(
    column(4,
           div(textOutput("lab_avg_out"), style = "color: blue;"))),
  hr(),
  fluidRow(
    column(12,
           HTML("<b>Quizzes </b><br/> 
                Enter a percentage grade for each quiz <i>(e.g. enter 75 if you got 75%). </i></br/><br/> 
                Quiz 11 can optionally be completed in replacement of your lowest quiz score <i>(for a total of 9 graded quiz submissions).</i><br/>
                <b>The lowest quiz grade will be automatically dropped.</b><br/><br/>")),
    column(2,
           numericInput("q1", "Quiz 1", value = NA, min = 0, max = 100, step = 1)),
    column(2,
           numericInput("q2", "Quiz 2", value = NA, min = 0, max = 100, step = 1)),
    column(2,
           numericInput("q3", "Quiz 3", value = NA, min = 0, max = 100, step = 1)),
    column(2,
           numericInput("q4", "Quiz 4", value = NA, min = 0, max = 100, step = 1)),
    column(2,
           numericInput("q5", "Quiz 5", value = NA, min = 0, max = 100, step = 1))),
  fluidRow(
    column(2,
           numericInput("q6", "Quiz 6", value = NA, min = 0, max = 100, step = 1)),
    column(2,
           numericInput("q7", "Quiz 7", value = NA, min = 0, max = 100, step = 1)),
  	column(2,
			numericInput("q8", "Quiz 8", value = NA, min = 0, max = 100, step = 1)),
  	column(2,
			numericInput("q9", "Quiz 9", value = NA, min = 0, max = 100, step = 1)),
    column(2,
      numericInput("q10", "Quiz 10", value = NA, min = 0, max = 100, step = 1))),
  fluidRow(
    column(2,
           numericInput("q11", "Quiz 11", value = NA, min = 0, max = 100, step = 1))),
  fluidRow(
    column(4,
           div(textOutput("quiz_avg_out"), style = "color: blue;"))),

  hr(),
  fluidRow(
    column(12,
           HTML("<b>Tests</b>
           <br/>Enter the percentage grade received for each test. <i>(e.g. __/33 = __%)</i> <br><br>
           <i>If applicable,</i> add your 3 extra credit points to the appropriate exam.
           </br><b>Guess grades for tests not yet completed to see how it will affect your overall grade. </b><br><br>")),
    column(2,
           numericInput("m1", "Midterm 1", value = 50, min = 0, max = 100)),
    column(2,
           numericInput("m2", "Midterm 2", value = 50, min = 0, max = 100)),
    column(2,
           numericInput("final", "Final", value = 50, min = 0, max = 100))
           ),
  hr(),
  fluidRow(
    column(12,
           HTML("<b>Miscellaneous</b><br/> 
                Enter an integer for the participation opportunities missed and a percentage grade (0-100) for the data project.<br/><br/>")),
    column(3,
           numericInput(("opp_missed"), "Participation Opportunities Missed", value = 0, min = 0, max = 10)),
    column(3,
           numericInput(("group"), "Data Skills Demonstration Project", value = 50, min = 0, max = 100)),
	),
  hr(),
  fluidRow(
    column(12,
           div(textOutput("weighted_avg"), style = "color: blue;")),
    column(12,
           div(textOutput("letter_grade"), style = "color: blue;")),),
  div(style = "height: 100px;"))


#--------------------------------------------------------------------------------------------------------------------------------------------
# Define server logic 
server <- function(input, output) {
  
  ### Defining Weights of Categories
  # participation_weight <- 0.05
  # lab_weight <- 0.10
  # quiz_weight <- 0.15
  # mt1_weight <- 0.15
  # mt2_weight <- 0.15
  # final_weight <- 0.20
  # proj_weight <- 0.20
  # ec_weight <- 0.02
  # 
  # weights <- c(participation_weight, lab_weight, quiz_weight, mt1_weight, 
  #              mt2_weight, final_weight, proj_weight, ec_weight)
  
  

  #### Define Average/Drop Function
  avg_drop_x_lowest <- function(values, drops=0) {
    if (sum(!is.na(values)) <= drops) {
      return(NA)
    } else if (drops == 0) {
      return(round(sum(values, na.rm = T) / (sum(!is.na(values))), 2))
    } else {
      return(round((sum(values, na.rm = T) - sum(sort(values)[1:drops])) / (sum(!is.na(values)) - drops), 2))
    }
  }
  
  

  ##### LAB
  lab_avg <- reactive({
    lab_inputs <- c(input$lab01, input$lab02, input$lab03, input$lab04, input$lab05,
                    input$lab06, input$lab07, input$lab08, input$lab09, input$lab10)
    lab11 <- input$lab11
    
    # Count only labs that are not "Unknown" for early-exit logic
    n_non_unknown <- sum(lab_inputs %in% c("Completed", "Not Completed")) + 
      ifelse(lab11 %in% c("Completed", "Not Completed"), 1, 0)
    if (n_non_unknown < 2) return(NA)
    
    # Assign numeric scores
    lab_scores <- ifelse(lab_inputs == "Completed", 100,
                         ifelse(lab_inputs %in% c("Not Completed", "Unknown"), 0, NA))
    lab_scores <- as.numeric(lab_scores)
    lab11_score <- ifelse(lab11 == "Completed", 100,
                          ifelse(lab11 %in% c("Not Completed", "Unknown"), 0, NA))
    lab11_score <- as.numeric(lab11_score)
    
    base_labs <- lab_scores[!is.na(lab_scores)]
    
    if (!is.na(lab11_score) && lab11_score > min(base_labs)) {
      all_labs <- c(base_labs, lab11_score)
      drops <- 2
    } else {
      all_labs <- base_labs
      drops <- 1
    }
    
    return(avg_drop_x_lowest(all_labs, drops = drops))
  })

  output$lab_avg_out <- renderText({
    score <- lab_avg()
    if (is.na(score)) {
      return("Lab Mean: Add more estimated scores!")
    } else {
      return(paste0("Lab Mean: ", score, "%"))
    }
  })


  ##### QUIZ
  quiz_avg <- reactive({
    quiz_inputs <- c(input$q1, input$q2, input$q3, input$q4, input$q5,
                     input$q6, input$q7, input$q8, input$q9, input$q10)
    quiz11 <- input$q11
    
    # Count only quizzes that are not NA
    n_non_na <- sum(!is.na(quiz_inputs)) + ifelse(!is.na(quiz11), 1, 0)
    if (n_non_na < 2) return(NA)
    
    quiz_scores <- as.numeric(replace(quiz_inputs, is.na(quiz_inputs), 0))
    quiz11_score <- ifelse(is.na(quiz11), NA, as.numeric(quiz11))
    
    base_quizzes <- quiz_scores
    
    # Use Quiz 11 only if it improves the score
    if (!is.na(quiz11_score) && quiz11_score > min(base_quizzes)) {
      all_quizzes <- c(base_quizzes, quiz11_score)
      drops <- 2
    } else {
      all_quizzes <- base_quizzes
      drops <- 1
    }
    
    return(avg_drop_x_lowest(all_quizzes, drops = drops))
  })

  output$quiz_avg_out <- renderText({
    score <- quiz_avg()
    if (is.na(score)) {
      return("Quiz Mean: Add more estimated scores!")
    } else {
      return(paste0("Quiz Mean: ", score, "%"))
    }
  })

  ##### Original Grading Policy Weighted
  original <- reactive({

    participation_weight <- 0.05
    lab_weight <- 0.10
    quiz_weight <- 0.15

    mt1_weight <- 0.15
    mt2_weight <- 0.15
    final_weight <- 0.20

    project_weight <- 0.20
    extra_credit_weight <- 0.02

    participation_percent <- 100
    
    
    if (input$opp_missed > 1) {
      participation_percent <- ((17 - (input$opp_missed - 1)) / 17) * 100
    }
    final <- ifelse(is.na(input$final), 0, input$final)
    
    weight_avg <- (participation_weight * participation_percent) + 
      (lab_avg() * lab_weight) + 
      (quiz_avg() * quiz_weight) +
      (input$m1 * mt1_weight) + 
      (input$m2 * mt2_weight) + 
      (input$final * final_weight) +
      (input$group * project_weight) 

    return(weight_avg)
  })

  #### Grade Estimate
  
    output$weighted_avg <- renderText({
      score <- original()
      if (is.na(score)) {
        return("Grade Estimate: Add more estimated scores!")
      } else {
        return(paste0("Grade Estimate: ", score, "%"))
      }
    })
  
  #   output$letter_grade <- renderText({
  #     paste0("Letter grade: ", case_when(original() >= 98.5 ~ "A+",
  #                                        original() < 98.5 & original() >= 94.0 ~ "A",
  #                                        original() < 94.0 & original() >= 89.0 ~ "A-",
  #                                        original() < 89.0 & original() >= 85.0 ~ "B+",
  #                                        original() < 85.0 & original() >= 81.0 ~ "B",
  #                                        original() < 81.0 & original() >= 75.5 ~ "B-",
  #                                        original() < 75.5 & original() >= 70.5 ~ "C+",
  #                                        original() < 70.5 & original() >= 60.5 ~ "C",
  #                                        original() < 60.5 & original() >= 51 ~ "C",
  #                                        original() < 51.0 ~ "D")
  #     )
  # })


}


# Run the application 
shinyApp(ui = ui, server = server)
