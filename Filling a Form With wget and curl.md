# Filling forms

## Save webpage

#### Using wget:

```wget http://example.com > file.txt```
#### Using cURL

```curl http://example.com > file.txt```

## Submiting filled form

#### Using wget:
```wget --post-data 'Name=Lee&Age=36&Town=The%20Internet' https://example.com/page-two.php```

#### Using cURL
```curl -d Name="Lee" -d Age="36" -d Town="The Internet" https://example.com/page-two.php > ~/Desktop/form-response.html```
