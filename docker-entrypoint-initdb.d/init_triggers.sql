CREATE OR REPLACE FUNCTION set_default_price() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.price IS NULL THEN
        NEW.price := 0;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_insert_price
BEFORE INSERT ON products_unifiedproduct
FOR EACH ROW EXECUTE FUNCTION set_default_price();


CREATE OR REPLACE FUNCTION log_price_change() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.price IS DISTINCT FROM OLD.price THEN
        INSERT INTO products_priceupdatelog(product_id, old_price, new_price)
        VALUES (OLD.id, OLD.price, NEW.price);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER after_update_price
AFTER UPDATE ON products_unifiedproduct
FOR EACH ROW EXECUTE FUNCTION log_price_change();
