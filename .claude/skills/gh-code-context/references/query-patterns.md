# Search Query Patterns

Common patterns for effective code search across GitHub Enterprise.

## Function/Method Discovery

```bash
# Function definition (JavaScript/TypeScript)
"function functionName"
"const functionName = "
"export function functionName"
"async function functionName"

# Method definition (various languages)
"def method_name"           # Python
"func methodName"           # Go
"public void methodName"    # Java/C#

# Arrow functions
"const handleClick = () =>"
"const fetchData = async () =>"
```

## Class/Component Discovery

```bash
# Class definitions
"class ClassName"
"export class ClassName"
"class ClassName extends"

# React components
"function ComponentName("
"const ComponentName: React.FC"
"export default function ComponentName"

# Interfaces/Types
"interface InterfaceName"
"type TypeName ="
```

## Import/Dependency Tracking

```bash
# ES6 imports
"import { Symbol } from"
"import Symbol from"
"from '@org/package'"

# CommonJS
"require('package-name')"
"require('@org/package')"

# Python imports
"from module import"
"import module"
```

## Configuration Patterns

```bash
# Environment variables
"process.env.VARIABLE"
"os.environ"
"ENV['VARIABLE']"

# Config files
filename:config "settingName"
filename:.env "API_KEY"
extension:yaml "database:"
extension:json "apiEndpoint"
```

## API Endpoints

```bash
# REST endpoints
"@Get('/"
"@Post('/"
"app.get('/"
"router.post('/"

# GraphQL
"type Query"
"type Mutation"
"@Resolver"
```

## Error Handling

```bash
# Try-catch patterns
"catch (error)"
"except Exception"
"rescue StandardError"

# Custom errors
"class CustomError extends"
"raise CustomException"
```

## Test Files

```bash
# Test discovery
"describe('" 
"it('should"
"test('"
"def test_"
"@Test"

# Find tests for specific function
"describe('functionName"
"test_function_name"
```

## Authentication/Security

```bash
# Auth implementations
"authenticate"
"authorization"
"jwt.verify"
"bcrypt.compare"

# Permission checks
"hasPermission"
"isAuthorized"
"checkAccess"
```

## Database Queries

```bash
# SQL patterns
"SELECT * FROM"
"INSERT INTO"
"UPDATE table SET"

# ORM patterns
"Model.find"
"prisma.table"
".where("
".findOne("
```

## Multi-Word Exact Match

Use quotes for exact phrases:
```bash
"user authentication service"
"handle form submission"
```

## Excluding Patterns

Search for A but not in test files:
```bash
# First search broadly
"functionName" --limit 50

# Then filter results by path (in post-processing)
# Exclude: *test*, *spec*, *mock*
```

## Language-Specific Tips

### TypeScript/JavaScript
- Search for type definitions: `"interface IUser"` or `"type User ="`
- Find hooks: `"const use" --language typescript`
- Find exports: `"export { " --language typescript`

### Python
- Find decorators: `"@decorator_name"`
- Find class methods: `"def method_name(self"`
- Find async: `"async def"`

### Go
- Find structs: `"type StructName struct"`
- Find interfaces: `"type InterfaceName interface"`
- Find handlers: `"func.*Handler"`

## Combining for Context

To understand a feature end-to-end:

1. Find the entry point: `"route: '/feature'" --owner org`
2. Find the handler: `"handleFeature" --owner org`
3. Find the service: `"FeatureService" --owner org`
4. Find the tests: `"describe('Feature" --owner org`
