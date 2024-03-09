# Define a function named get_title that takes three parameters: first_name, last_name, and job.
def get_title(first_name, last_name, job):
    # Concatenate the first_name, last_name, and job to form a title.
    title = first_name + " " + last_name + " the " + job
    # Return the generated title.
    return title

# Define a function named test that takes three parameters: first_name, last_name, and job.
def test(first_name, last_name, job):
    # Call the get_title function with the provided parameters and assign the returned title to the variable title.
    title = get_title(first_name, last_name, job)
    # Print the first_name, last_name, job, and title.
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    # Print a separator line for readability.
    print("=====================================")

# Call the test function with different parameters to test the get_title function.
test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")