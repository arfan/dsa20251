from dynamic_array_stack import DynamicArrayStack


def infix_to_postfix(infix_expression):
    """
    Convert infix expression to postfix expression using a stack.
    
    Args:
        infix_expression (str): The infix expression to convert
        
    Returns:
        str: The postfix expression
    """
    
    def get_precedence(operator):
        """
        Get the precedence of an operator.
        Higher number means higher precedence.
        """
        precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '**': 3  # Python exponentiation
        }
        return precedence.get(operator, 0)
    
    def is_operator(char):
        """Check if a character is an operator."""
        return char in ['+', '-', '*', '/', '^']
    
    def is_operand(char):
        """Check if a character is an operand (alphanumeric)."""
        return char.isalnum()
    
    # Initialize stacks
    operator_stack = DynamicArrayStack(initial_capacity=10)
    output = []  # Output list to store postfix expression
    
    print(f"🔄 Converting infix to postfix: '{infix_expression}'")
    print("Step-by-step process:")
    print("-" * 60)
    
    i = 0
    while i < len(infix_expression):
        char = infix_expression[i]
        
        # Skip whitespace
        if char == ' ':
            i += 1
            continue
            
        print(f"Processing character: '{char}'")
        
        # Case 1: Character is an operand
        if is_operand(char):
            output.append(char)
            print(f"  → Operand found: Added '{char}' to output")
            print(f"  → Current output: {output}")
        
        # Case 2: Character is an operator
        elif is_operator(char):
            # If operator stack is empty, push operator
            if operator_stack.isEmpty():
                operator_stack.push(char)
                print(f"  → Operator stack empty: Pushed '{char}' to operator stack")
            else:
                # Check precedence and pop operators accordingly
                while (not operator_stack.isEmpty() and 
                       operator_stack.peek() != '(' and
                       get_precedence(operator_stack.peek()) >= get_precedence(char)):
                    
                    popped_op = operator_stack.pop()
                    output.append(popped_op)
                    print(f"  → Popped '{popped_op}' from operator stack to output")
                
                operator_stack.push(char)
                print(f"  → Pushed '{char}' to operator stack")
        
        # Case 3: Character is opening bracket '('
        elif char == '(':
            operator_stack.push(char)
            print(f"  → Opening bracket: Pushed '{char}' to operator stack")
        
        # Case 4: Character is closing bracket ')'
        elif char == ')':
            print(f"  → Closing bracket found: Popping until '('")
            while not operator_stack.isEmpty() and operator_stack.peek() != '(':
                popped_op = operator_stack.pop()
                output.append(popped_op)
                print(f"    → Popped '{popped_op}' from operator stack to output")
            
            # Pop the opening bracket '(' but don't add to output
            if not operator_stack.isEmpty():
                opening_bracket = operator_stack.pop()
                print(f"    → Found and removed matching '(' from operator stack")
        
        # Display current state
        print(f"  → Output so far: {output}")
        if not operator_stack.isEmpty():
            print(f"  → Operator stack top: '{operator_stack.peek()}'")
        else:
            print(f"  → Operator stack: empty")
        print()
        
        i += 1
    
    # Pop remaining operators from stack
    print("🔚 Processing remaining operators in stack:")
    while not operator_stack.isEmpty():
        popped_op = operator_stack.pop()
        output.append(popped_op)
        print(f"  → Popped '{popped_op}' from operator stack to output")
    
    postfix_result = ''.join(output)
    print(f"✅ Final postfix expression: '{postfix_result}'")
    print("-" * 60)
    
    return postfix_result


def test_infix_to_postfix():
    """Test the infix to postfix converter with various expressions."""
    
    test_cases = [
        "a+b*c",           # Simple expression
        "a+b*c-d",         # Multiple operators
        "(a+b)*c",         # Parentheses
        "a+b*(c-d)",       # Nested operations
        "a+b*c+d",         # Same precedence
        "a*(b+c*d)+e",     # Complex expression
        "((a+b)*c)",       # Multiple parentheses
        "a*b+c/d-e",       # Mixed operators
        "(a+b)*(c-d)",     # Multiple parentheses with operations
    ]
    
    print("🧪 Testing Infix to Postfix Conversion")
    print("=" * 70)
    
    for i, expression in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        result = infix_to_postfix(expression)
        print(f"Infix:   {expression}")
        print(f"Postfix: {result}")
        print("=" * 70)


def interactive_converter():
    """Interactive infix to postfix converter."""
    
    print("\n" + "🎯 Interactive Infix to Postfix Converter" + "\n")
    print("Enter infix expressions to convert (or 'quit' to exit)")
    print("Supported operators: +, -, *, /, ^")
    print("Supported operands: letters and numbers")
    print("Parentheses: ( )")
    print("-" * 50)
    
    while True:
        try:
            expression = input("\nEnter infix expression: ").strip()
            
            if expression.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not expression:
                print("Please enter a valid expression.")
                continue
            
            result = infix_to_postfix(expression)
            print(f"\n📝 Summary:")
            print(f"Infix:   {expression}")
            print(f"Postfix: {result}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with a valid expression.")


# Main execution
if __name__ == "__main__":
    # Run automated tests
    test_infix_to_postfix()
    
    # Run interactive converter
    interactive_converter()
