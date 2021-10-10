def first_name
    split(' ').first
end

def last_name
    split(' ').drop(1).join(' ')
end


